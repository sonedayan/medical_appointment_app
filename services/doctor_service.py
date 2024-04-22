from fastapi import HTTPException, status
from schemas.doctor import doctors, Doctors, CreateAndEditADoctor

class DoctorService:
    @staticmethod
    def display_doctors(doctor_data):
        data = []
        for doctor in doctor_data:
            data.append(doctors[doctor])
        return data
    
    @staticmethod
    def get_doctor_by_id(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found', status_code=status.HTTP_404_NOT_FOUND)
        return doctor
    
    @staticmethod
    def create_doctor(doctor_data: CreateAndEditADoctor):
        id = len(doctors)
        doctor = Doctors(id=id, **doctor_data.model_dump())
        doctors[id] = doctor
        return doctor
    
    @staticmethod
    # Update a Single Doctor
    def update_doctor(doctor_data: CreateAndEditADoctor):
        id = len(doctors)
        doctor = Doctors(id=id, **doctor_data.model_dump())
        doctors[id] = doctor
        return doctor
    
    @staticmethod
    # Delete a Single Doctor
    def delete_doctor(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found', status_code=status.HTTP_404_NOT_FOUND)
        del doctors[doctor_id]
        return {"message": "Doctor deleted successfully", "data": doctor}