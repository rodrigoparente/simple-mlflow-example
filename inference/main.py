# Python libraries
import os
from dotenv import load_dotenv

# Third-party libraries
import uvicorn
import mlflow
import numpy as np
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from mlflow.exceptions import MlflowException

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables for MLflow configuration
TRACKING_URI = os.getenv('TRACKING_URI')
REGISTERED_MODEL_NAME = os.getenv('REGISTERED_MODEL_NAME')
REGISTERED_MODEL_ALIAS = os.getenv('REGISTERED_MODEL_ALIAS')

# Configure MLflow tracking
mlflow.set_tracking_uri(TRACKING_URI)

# Initialize FastAPI application
app = FastAPI()

# Initialize a variable to hold the model
model = None


# Function to load the MLflow model
def load_model():
    global model
    try:
        model_path = f'models:/{REGISTERED_MODEL_NAME}@{REGISTERED_MODEL_ALIAS}'
        model = mlflow.pyfunc.load_model(model_path)
        print(f"Model {REGISTERED_MODEL_NAME}@{REGISTERED_MODEL_ALIAS} loaded successfully.")
    except MlflowException as e:
        print(f"Error loading model: {e}")
        model = None


# Define a Pydantic model for the input data (array of arrays)
class PredictionInput(BaseModel):
    data: list[list[float]]


# Health check endpoint
@app.get('/health')
async def health_check():
    if model is None:
        return {"status": "unhealthy", "details": "Model is not loaded."}
    return {"status": "healthy", "details": "Model is loaded and service is running."}


# Reload model endpoint
@app.post('/reload-model')
async def reload_model():
    try:
        load_model()
        if model:
            return {"status": "success", "details": "Model reloaded successfully."}
        else:
            raise HTTPException(status_code=500, detail="Failed to reload model.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define the prediction endpoint
@app.post('/predict')
async def predict(input_data: PredictionInput):
    global model

    # Check if model is loaded, if not, attempt to load it
    if model is None:
        load_model()

    # If model still not loaded, return an error
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded. Please check the model registration and alias.")

    try:
        # Extract the input data (array of arrays)
        input_array = np.array(input_data.data)

        # Make a batch prediction using the loaded model
        predictions = model.predict(input_array)

        # Return the predictions as a JSON response
        return {'predictions': predictions.tolist()}

    except Exception as e:
        # Handle any exceptions and return an error response
        raise HTTPException(status_code=400, detail=str(e))


# Entry point for running the FastAPI app
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
