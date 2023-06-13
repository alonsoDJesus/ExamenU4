import uvicorn
from fastapi import FastAPI
from Diabetes import Diabetes
import numpy as np
import pickle
import pandas as pd 

app = FastAPI()
pickle_in = open("svc.pkl", "rb")
svc = pickle.load(pickle_in)

@app.post("/predict")
def predict_diabetes(data: Diabetes):
    data = data.dict()
    
    pregnancies = data["pregnancies"]
    glucose = data["glucose"]
    blood_pressure = data["blood_pressure"]
    skin_thickness = data["skin_thickness"]
    insuline = data["insuline"]
    bmi = data["bmi"]
    diabetes_pf = data["diabetes_pf"]
    age = data["age"]
    
    prediction = svc.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insuline, bmi, diabetes_pf, age]])
    
    if(prediction[0] > 0.5):
        prediction = "positivo a diabetes"
    
    else:
        prediction = "negativo a diabetes"
        
    return {'prediction': prediction}

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
    