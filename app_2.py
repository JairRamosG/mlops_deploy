from fastapi import FastAPI, HTTPException
from Houses import House
from joblib import load
import pandas as pd


app = FastAPI()

classifier = load('linear_regression.joblib')

@app.get('/')
def read_root():
    return {"message": "Hello World"}

@app.post('/predict/')
def predict(data: House):
    df = pd.DataFrame([data.dict()])
    predictions = classifier.predict(df)

    return {
            'predictions' : predictions.tolist()
    }
