from fastapi import APIRouter, status, HTTPException
from schemas.patient import PatientsCreateAndEdit, patients
from services.patient_service import PatientService

patient_router = APIRouter()

@patient_router.get("/",status_code=status.HTTP_200_OK)
def get_all_patients():
    data = PatientService.display_patients(patient_data=patients)
    return {'message': 'Successfully retrieved patients', 'data': data}

@patient_router.get("/{patient_id}",status_code=status.HTTP_200_OK)
def get_patient_by_id(patient_id: int):
    data = PatientService.get_patient_by_id(patient_id)
    return {'message': 'Successfully retrieved a single patient', 'data': data}

@patient_router.post("/",status_code=status.HTTP_201_CREATED)
def create_patient(patient_data: PatientsCreateAndEdit):
    data = PatientService.create_patient(patient_data)
    return {'message': 'Successfully created a new patient', 'data': data}

@patient_router.put("/{patient_id}",status_code=status.HTTP_200_OK)
def update_patient(patient_id: int, patient_data: PatientsCreateAndEdit):
    data = PatientService.update_patient(patient_data)
    return {'message': 'Successfully updated a patient', 'data': data}

@patient_router.delete("/{patient_id}",status_code=status.HTTP_200_OK)
def delete_patient(patient_id: int):
    data = PatientService.delete_patient(patient_id)
    return {'message': 'Successfully deleted a patient', 'data': data}



