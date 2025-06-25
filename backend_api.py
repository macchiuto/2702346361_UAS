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

@app.post("/predict")
def predict(data: ObesityData):
    input_array = np.array([[
        data.Gender, data.Age, data.Height, data.Weight,
        data.family_history_with_overweight, data.FAVC,
        data.FCVC, data.NCP, data.CAEC, data.SMOKE,
        data.CH2O, data.SCC, data.FAF, data.TUE,
        data.CALC, data.MTRANS
    ]])
    prediction = pipeline.predict(input_array)
    pred_label = label_encoder.inverse_transform(prediction)[0]
    return {"prediction": pred_label}

