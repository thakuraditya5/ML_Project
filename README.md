# End-to-End MLOps Wine Quality Prediction

## 🚀 Project Overview

This project demonstrates a production-grade **MLOps (Machine Learning Operations)** pipeline for deploying a Machine Learning model. The goal is to predict wine quality based on physicochemical properties using the Wine dataset.

The core focus is not just on the model, but on the **engineering practices** that ensure reliability, reproducibility, and automation:
- **Continuous Integration (CI)**: Automated checks for code quality and testing.
- **Continuous Delivery (CD)**: Automated containerization and deployment.
- **Experiment Tracking**: Systematic logging of model parameters and metrics.

## 🛠️ Technology Stack

- **Model**: Scikit-Learn (Random Forest)
- **API**: FastAPI
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Execution Environment**: Windows / Linux
- **Experiment Tracking**: MLflow

## 🏗️ Architecture

1.  **Code Changes**: Developer pushes code to GitHub.
2.  **CI Pipeline**: GitHub Actions triggers:
    - Linting (Flake8)
    - Formatting (Black)
    - Testing (Pytest)
3.  **Experiment Tracking**: Training runs log metrics and artifacts to MLflow.
4.  **CD Pipeline**: Upon success, a Docker image is built and pushed to **Docker Hub**.
5.  **Deployment**: The API can be pulled and run anywhere using Docker.

## 💻 How to Run Locally

### Prerequisites
- Python 3.9+
- Docker (optional, for container run)

### 1. Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd mlops-project-1

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. Run Tests & Checks
Using the included `make.bat` (Windows) or `Makefile` (Linux):
```bash
make lint    # Check code style
make format  # Auto-format code
make test    # Run unit tests
```

### 3. Experiment Tracking
Train the model and log to MLflow:
```bash
python train_model.py
mlflow ui
# Open http://127.0.0.1:5000 in your browser
```

### 4. Run the API
```bash
uvicorn app:app --reload
# Access API docs at http://127.0.0.1:8000/docs
```

### 5. Docker Run
```bash
docker build -t wine-quality-api .
docker run -p 8000:8000 wine-quality-api
```

## 📦 Deployment (CI/CD)

The `.github/workflows/ci.yml` file automates the pipeline. To enable Docker Hub pushing:
1.  Go to GitHub Repo Settings -> Secrets and variables -> Actions.
2.  Add `DOCKERHUB_USERNAME`.
3.  Add `DOCKERHUB_TOKEN` (Create an Access Token in Docker Hub Settings).
