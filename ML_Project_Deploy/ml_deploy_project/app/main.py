from fastapi import FastAPI
import pickle
import numpy as np

# Load trained model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to ML Model API"}

@app.post("/predict")
def predict(features: list):
    prediction = model.predict(np.array(features).reshape(1, -1))
    return {"prediction": prediction.tolist()}
