# Simple MLFLOW Example

This project consists of two containers: one for the MLflow tracking server and another for an inference service built with FastAPI. Additionally, it includes a Jupyter notebook that demonstrates the process of logging training information, registering runs, and managing models in MLflow.

## Project Structure

- **mlflow/**: Contains the Dockerfile for the MLflow server.
- **inference/**: Contains the Dockerfile for the inference service using FastAPI.
- **notebook.ipynb**: Jupyter notebook for logging and model management.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python (for running the Jupyter notebook)

### Steps to Execute

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies** for the Jupyter notebook:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build and run the containers** using Docker Compose:
   ```bash
   docker-compose up --build -d
   ```

   This command will create the necessary Docker containers for both the MLflow server and the FastAPI inference service.

4. **Run the Jupyter notebook**:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open the `notebook.ipynb` file located in the root folder and follow the instructions within the notebook to log training information and manage models in MLflow.

5. **Access the MLflow UI**:
   Open your web browser and navigate to [http://localhost:8080](http://localhost:8080) to view the MLflow UI.


6. **Make predictions using the FastAPI inference service**:
   Use the provided endpoints in the inference service to make predictions based on the models registered in MLflow. The swagger for the inference service is accessible at [http://localhost:5000/docs](http://localhost:5000/docs).

## License

This project is licensed under the MIT License.