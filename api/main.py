from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "best_model.joblib"
model = joblib.load(MODEL_PATH)

app = FastAPI(title="Toronto Bike Share Demand Predictor")


class DayInput(BaseModel):
    temp: float = Field(..., description="Mean temperature in °C")
    rain: float = Field(0, ge=0, description="Rain in mm")
    snow: float = Field(0, ge=0, description="Snowfall in cm")
    wind: float = Field(15, ge=0, description="Max wind speed in km/h")
    weekday: int = Field(..., ge=0, le=6, description="0 = Monday ... 6 = Sunday")
    month: int = Field(..., ge=1, le=12)


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(day: DayInput):
    row = pd.DataFrame([{
        "temp": day.temp,
        "rain": day.rain,
        "snow": day.snow,
        "wind": day.wind,
        "weekday": day.weekday,
        "month": day.month,
        "is_weekend": int(day.weekday >= 5),
    }])
    prediction = model.predict(row)[0]
    return {"predicted_rides": int(round(prediction))}