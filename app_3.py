from fastapi import FastAPI, HTTPException
from Houses import House
from joblib import load
import pandas as pd


app = FastAPI()

classifier = load('linear_regression.joblib') 

x_test = pd.read_csv('xtest.csv')
features = pd.read_csv('selected_features.csv') 
features = features['0'].tolist() # Eliminar la primera columna que es el índice
x_test = x_test[features]



@app.get('/')
def read_root():
    return {"message": "Hello World"}

@app.post('/predict/')
def predict():
    predictions = classifier.predict(x_test)
    return {
        'predictions': predictions.tolist()
        }