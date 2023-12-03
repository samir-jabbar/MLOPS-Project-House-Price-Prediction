# MLOPS Project - House Price Prediction

This repository contains the code and resources for a Machine Learning Operations (MLOps) project focused on predicting house prices. The project utilizes both FastAPI and Flask for building REST APIs, and the machine learning models are tracked and managed using MLflow. Additionally, the models are saved in the ONNX format for interoperability.

## Project Structure

The project is organized into several directories:

- **data:** Contains the dataset for house price prediction (`kc_house_data.csv`).
- **fastapi:** Implementation of the FastAPI application.
- **flask:** Implementation of the Flask application.
- **flask_docker:** Dockerfile and related files for Flask application containerization.
- **mlflow:** Code related to MLflow tracking and model training.
- **preprocessing.pkl:** Pickle file containing the preprocessing transformations.
- **docker-compose.yml:** Docker Compose file for orchestrating FastAPI and Flask containers.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/samir-jabbar/MLOPS-Project-House-Price-Prediction.git

Navigate to Project Root:

cd MLOPS-Project-House-Price-Prediction

Explore Project Components:

data: Contains the dataset.

fastapi: FastAPI application.

flask: Flask application.

flask_docker: Dockerfile for Flask application.

mlflow: MLflow tracking and model training code.

preprocessing.pkl: Pickle file for preprocessing transformations.

docker-compose.yml: Docker Compose file.

Running the Project

Run Docker Compose:

docker-compose up

Access APIs:

FastAPI: http://localhost:8000/docs

Flask: http://localhost:5000

