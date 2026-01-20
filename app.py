from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from typing import List

# Load the model directly
model = joblib.load("model.joblib")


# Define the input data structure based on Scikit-learn Wine dataset features
class WineFeatures(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float


app = FastAPI(title="Wine Quality Prediction API")


@app.get("/")
def home():
    return {
        "message": "Welcome to the Wine Quality Prediction API. Use /predict to get predictions."
    }


@app.post("/predict")
def predict(features: WineFeatures):
    try:
        # Convert input features to dictionary
        input_data = features.model_dump()

        # Rename the field that has a slash in the dataset but underscore in Pydantic
        input_data["od280/od315_of_diluted_wines"] = input_data.pop(
            "od280_od315_of_diluted_wines"
        )

        # Create DataFrame
        # We ensure the order matches the model's expectations using feature_names_in_ if available
        # But simply creating DataFrame with correct columns is usually enough for sklearn
        data = pd.DataFrame([input_data])

        # Reorder columns to match training data
        if hasattr(model, "feature_names_in_"):
            data = data[model.feature_names_in_]

        prediction = model.predict(data)
        prediction_prob = model.predict_proba(data)

        return {
            "prediction": int(prediction[0]),
            "probability": prediction_prob[0].tolist(),
        }
    except Exception as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
