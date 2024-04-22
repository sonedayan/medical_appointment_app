from fastapi import HTTPException

from schemas.patient import patients
from schemas.appointment import Appointments, CreateAppointments, appointments

class AppointmentService:
    @staticmethod
    def create_appointment(appointment_data: CreateAppointments):
        id = len(appointments)
        patient = patients.get(appointment_data.id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        # appointments.append(Appointments(id=id, patient_id=appointment_data.id, patient_name=patient.patient_name, doctor_id=appointment_data.doctor_id, doctor_name=appointment_data.doctor_name, appointment_date=appointment_data.appointment_date, appointment_time=appointment_data.appointment_time))
    
    @staticmethod
    def get_appointments(appointment_data):
        data = []
        for appointment in appointment_data:
            data.append(appointments[appointment])
        return data