from fastapi import FastAPI, WebSocket
import fhir_handler
import chatbot_handler

app = FastAPI()

@app.get("/")
def home():
    return {"message": "InstaMed Backend Running!"}

# FHIR Endpoints
@app.post("/fhir/patient")
def create_patient(patient_id: str, name: str, gender: str, birth_date: str):
    return fhir_handler.create_fhir_patient(patient_id, name, gender, birth_date)

@app.post("/fhir/diagnostic_report")
def create_diagnostic_report(patient_id: str, report_text: str):
    return fhir_handler.create_fhir_diagnostic_report(patient_id, report_text)

# Chatbot WebSocket (Not visible in /docs, must be tested via WebSocket client)
@app.websocket("/ws/chatbot")
async def chatbot_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = chatbot_handler.chatbot_response(data)
        await websocket.send_text(response)
