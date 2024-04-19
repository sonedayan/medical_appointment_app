from fastapi import APIRouter, status
from schemas.doctor import doctors
from services.doctor_service import DoctorService

doctor_router = APIRouter()

@doctor_router.get("/", status_code=status.HTTP_200_OK)
def get_all_doctors():
    data = DoctorService.display_doctors(doctor_data=doctors)
    return {"message": "Successfully retrieved all doctors information", "data": data}