from fastapi import APIRouter, status
from schemas.doctor import CreateAndEditADoctor, doctors
from services.doctor_service import DoctorService

doctor_router = APIRouter()

@doctor_router.get("/", status_code=status.HTTP_200_OK)
def get_all_doctors():
    data = DoctorService.display_doctors(doctor_data=doctors)
    return {"message": "Successfully retrieved all doctors information", "data": data}

@doctor_router.get("/{doctor_id}", status_code=status.HTTP_200_OK)
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {"message": "Successfully retrieved doctor information", "data": data}

@doctor_router.post("/", status_code=status.HTTP_201_CREATED)
def create_doctor(doctor_data: CreateAndEditADoctor):
    data = DoctorService.create_doctor(doctor_data)
    return {"message": "Successfully created doctor", "data": data}

@doctor_router.put("/{doctor_id}", status_code=status.HTTP_200_OK)
def edit_doctor(doctor_id: int, doctor_data: CreateAndEditADoctor):
    data = DoctorService.update_doctor(doctor_data)
    return {"message": "Successfully edited doctor", "data": data}

@doctor_router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int):
    data = DoctorService.delete_doctor(doctor_id)
    return {"message": "Successfully deleted doctor", "data": data}