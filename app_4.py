from fastapi import FastAPI, HTTPException, UploadFile, File
from joblib import load
from io import StringIO
import pandas as pd


app = FastAPI()


@app.get('/')
def read_root():
    return {"message": "Hello World"}

@app.post('/predict/')
async def predict(file : UploadFile = File(...)):

    classifier = load('linear_regression.joblib') 
    features = pd.read_csv('selected_features.csv', header=None) 
    #features = features['0'].tolist() # Eliminar la primera columna que es el índice
    features = features.iloc[1:, 0].tolist() # Eliminar la primera columna que es el índice

    try:
        content = await file.read()
    
        df_completo = pd.read_csv(StringIO(content.decode('utf-8'))) # El formato en el que se recibe el archivo es bytes, por lo que se decodifica a utf-8 y luego se convierte a un DataFrame de pandas
        df_utilizado = df_completo[features]

        predictions = classifier.predict(df_utilizado)

        return {
            'predictions' : predictions.tolist()
        }
    
    except Exception as e:
        print(f'Error: {str(e)}')
        raise HTTPException(status_code=500, detail=str(e))