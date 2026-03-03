from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model (saved as `adtech_model.pkl` by `training.py`)
model = pickle.load(open("adtech_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Ad Prediction Server Running"}

@app.post("/predict")
def predict(age:int, device:int, time:int, interest:int):

    data = np.array([[age, device, time, interest]])

    probability = model.predict_proba(data)[0][1]

    return {
        "install_probability": float(probability)
    }