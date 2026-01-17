from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

print("🔥 CORRECT API FILE LOADED 🔥")

app = FastAPI(title="Student Performance Predictor")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class StudentInput(BaseModel):
    study_hours: float
    attendance: float
    previous_score: float

@app.get("/")
def home():
    return {"message": "ML Model API is running"}

@app.post("/predict")
def predict(data: StudentInput):
    X = np.array([[data.study_hours, data.attendance, data.previous_score]])
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    return {
        "prediction": "Pass" if prediction == 1 else "Fail",
        "probability": round(float(probability), 2)
    }
