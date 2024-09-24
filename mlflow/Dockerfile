# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file (if you have one) into the container
COPY requirements.txt .

# Install MLflow and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the MLflow server
EXPOSE 8080

# Command to run the MLflow server
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "8080"]