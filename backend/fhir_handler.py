from fhir.resources.patient import Patient
from fhir.resources.diagnosticreport import DiagnosticReport
from fhir.resources.observation import Observation
from fhir.resources.communication import Communication
from fhir.resources.careplan import CarePlan

def create_fhir_patient(patient_id, name, gender, birth_date):
    """Create a FHIR Patient resource"""
    patient = Patient.parse_obj({
        "id": patient_id,
        "resourceType": "Patient",
        "name": [{"use": "official", "family": name.split()[-1], "given": name.split()[:-1]}],
        "gender": gender,
        "birthDate": birth_date
    })
    return patient.json()

def create_fhir_diagnostic_report(patient_id, report_text, status="final"):
    """Create a FHIR DiagnosticReport resource"""
    diagnostic_report = DiagnosticReport.parse_obj({
        "resourceType": "DiagnosticReport",
        "status": status,
        "subject": {"reference": f"Patient/{patient_id}"},
        "text": {"status": "generated", "div": f"<div>{report_text}</div>"}
    })
    return diagnostic_report.json()
