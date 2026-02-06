from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

clf_model = joblib.load(os.path.join(BASE_DIR, "model.joblib"))
reg_model = joblib.load(os.path.join(BASE_DIR, "regression_model.joblib"))

app = FastAPI(
    title="Flight Delay Prediction API",
    version="1.0"
)

# ------------------ Schemas ------------------

class Model1Input(BaseModel):
    MONTH: int
    DAY: int
    SCHEDULED_ARRIVAL: int
    ARRIVAL_TIME: int
    ARRIVAL_DELAY: float
    SCHEDULED_DEPARTURE: int
    DEPARTURE_TIME: int
    DEPARTURE_DELAY: float
    DISTANCE: float
    AIR_TIME: float


class Model2Input(BaseModel):
    ARRIVAL_DELAY: float
    DEPARTURE_DELAY: float


# ------------------ Routes ------------------

@app.get("/")
def root():
    return {"status": "FastAPI running"}

@app.post("/predict_delay")
def predict_delay(data: Model1Input):
    features = [[
        data.MONTH,
        data.DAY,
        data.SCHEDULED_ARRIVAL,
        data.ARRIVAL_TIME,
        data.ARRIVAL_DELAY,
        data.SCHEDULED_DEPARTURE,
        data.DEPARTURE_TIME,
        data.DEPARTURE_DELAY,
        data.DISTANCE,
        data.AIR_TIME
    ]]
    pred = int(clf_model.predict(features)[0])
    return {"delay": pred}

@app.post("/predict_delay_minutes")
def predict_delay_minutes(data: Model2Input):
    try:
        features = [[
            float(data.ARRIVAL_DELAY),
            float(data.DEPARTURE_DELAY)
        ]]

        print("DEBUG features:", features)
        print("DEBUG model:", reg_model)

        minutes = reg_model.predict(features)

        print("DEBUG raw prediction:", minutes)

        return {"delay_minutes": round(float(minutes.flatten()[0]), 2)}

    except Exception as e:
        print("❌ ERROR:", repr(e))
        return {"error": str(e)}

