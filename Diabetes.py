from pydantic import BaseModel
class Diabetes(BaseModel):
    
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insuline: float
    bmi: float
    diabetes_pf: float
    age: float
    