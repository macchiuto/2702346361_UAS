from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load model pipeline
with open('xgb_pipeline.pkl', 'rb') as file:
    saved_data = pickle.load(file)
    pipeline = saved_data['pipeline']
    label_encoder = saved_data['label_encoder']
    obesity_levels = saved_data['obesity_levels']

app = FastAPI()

# Define input schema
class ObesityData(BaseModel):
    Age: float
    Height: float
    Weight: float
    Gender: str
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str

import pandas as pd

@app.post("/predict")
def predict(data: ObesityData):
    # Bikin dict input
    input_dict = {
        'Gender': [data.Gender],
        'Age': [data.Age],
        'Height': [data.Height],
        'Weight': [data.Weight],
        'family_history_with_overweight': [data.family_history_with_overweight],
        'FAVC': [data.FAVC],
        'FCVC': [data.FCVC],
        'NCP': [data.NCP],
        'CAEC': [data.CAEC],
        'SMOKE': [data.SMOKE],
        'CH2O': [data.CH2O],
        'SCC': [data.SCC],
        'FAF': [data.FAF],
        'TUE': [data.TUE],
        'CALC': [data.CALC],
        'MTRANS': [data.MTRANS],
    }
    # Convert ke DataFrame
    input_df = pd.DataFrame(input_dict)
    # Prediksi
    prediction = pipeline.predict(input_df)
    pred_label = label_encoder.inverse_transform(prediction)[0]
    return {"prediction": pred_label}
