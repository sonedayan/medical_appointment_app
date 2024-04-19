from fastapi import APIRouter, status, HTTPException
from schemas.patient import patients
from services.patient_service import PatientService

patient_router = APIRouter()

@patient_router.get("/",status_code=status.HTTP_200_OK)
def get_all_patients():
    data = PatientService.display_patients(patient_data=patients)
    return {'message': 'Successfully retrieved patients', 'data': data}



