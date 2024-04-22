from fastapi import HTTPException, status
from schemas.patient import Patients, PatientsCreateAndEdit, patients

class PatientService:
    @staticmethod
    # Get a list of patients
    def display_patients(patient_data):
        data = []
        for patient in patient_data:
            data.append(patients[patient])
        return data

    @staticmethod
    # Get a Single Patient
    def get_patient_by_id(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail="Patient not found", status_code=status.HTTP_404_NOT_FOUND)
        return patient
    
    @staticmethod
    # Get Post a Single Patient
    def create_patient(patient_data: PatientsCreateAndEdit):
       id = len(patients)
       patient = Patients(id=id, **patient_data.model_dump())
       patients[id] = patient
       return patient
    
    @staticmethod
    # Update a Single Patient
    def update_patient(patient_data: PatientsCreateAndEdit):
        id = len(patients)
        patient = Patients(id=id, **patient_data.model_dump())
        patients[id] = patient
        return patient
    
    @staticmethod
    # Delete a Single Patient
    def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail="Patient not found", status_code=status.HTTP_404_NOT_FOUND)
        del patients[patient_id]
        return {"message": "Patient deleted successfully", "data": patient}
