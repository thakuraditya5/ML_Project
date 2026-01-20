from fastapi.testclient import TestClient
from app import app, WineFeatures
import joblib
import os
import pytest

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Wine Quality Prediction API. Use /predict to get predictions."
    }


def test_predict():
    # Example feature set from the dataset
    features = {
        "alcohol": 13.2,
        "malic_acid": 1.78,
        "ash": 2.14,
        "alcalinity_of_ash": 11.2,
        "magnesium": 100.0,
        "total_phenols": 2.65,
        "flavanoids": 2.76,
        "nonflavanoid_phenols": 0.26,
        "proanthocyanins": 1.28,
        "color_intensity": 4.38,
        "hue": 1.05,
        "od280_od315_of_diluted_wines": 3.40,
        "proline": 1050.0,
    }

    response = client.post("/predict", json=features)
    assert response.status_code == 200
    json_response = response.json()
    assert "prediction" in json_response
    assert "probability" in json_response
    # Prediction should be an integer class (0, 1, or 2 for wine dataset)
    assert isinstance(json_response["prediction"], int)


def test_model_exists():
    assert os.path.exists("model.joblib")
