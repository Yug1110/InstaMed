from fastapi import FastAPI
import fhir_handler

app = FastAPI()

@app.get("/")
def home():
    return {"message": "InstaMed Backend Running!"}

@app.post("/fhir/patient")
def create_patient(patient_id: str, name: str, gender: str, birth_date: str):
    return fhir_handler.create_fhir_patient(patient_id, name, gender, birth_date)

@app.post("/fhir/diagnostic_report")
def create_diagnostic_report(patient_id: str, report_text: str):
    return fhir_handler.create_fhir_diagnostic_report(patient_id, report_text)
