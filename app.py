from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Health Kiosk ML API")

# Load models
logreg_model = joblib.load("logreg_model.joblib")
rf_model = joblib.load("rf_model.joblib")

# Input schema (must match dataset columns)
class PatientInput(BaseModel):
    age: float
    gender: str
    temp: float
    sys_bp: float
    dia_bp: float
    spo2: float
    hr: float
    fever: int
    cough: int
    fatigue: int
    chest_pain: int
    sob: int

@app.post("/predict")
def predict(data: PatientInput, model: str = "rf"):
    df = pd.DataFrame([data.dict()])

    m = logreg_model if model == "logreg" else rf_model

    pred = m.predict(df)[0]
    probs = m.predict_proba(df)[0]
    classes = list(m.classes_)

    top_idx = int(probs.argmax())
    return {
        "model_used": model,
        "predicted_disease": pred,
        "confidence": round(float(probs[top_idx]) * 100, 2),
        "all_probabilities": {
            classes[i]: round(float(probs[i]) * 100, 2)
            for i in range(len(classes))
        }
    }
