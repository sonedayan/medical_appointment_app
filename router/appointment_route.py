from fastapi import APIRouter, status, HTTPException
from schemas.appointment import Appointments, appointments
from services.appointment_service import AppointmentService

appointment_router = APIRouter()


@appointment_router.get('/', status_code=status.HTTP_200_OK)
def get_appointments():
    data = AppointmentService.get_appointments(appointment_data=appointments)
    return data


@appointment_router.post('/', status_code=status.HTTP_201_CREATED)
def create_appointment(appointment_data: Appointments):
    data = AppointmentService.create_appointment(appointment_data)
    return {"message": "Appointment created successfully", "data": data}