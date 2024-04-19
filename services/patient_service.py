from fastapi import HTTPException
from schemas.patient import Patients, patients

class PatientService:
    @staticmethod
    def display_patients(patient_data):
        data = []
        for patient in patient_data:
            data.append(patients[patient])
        return data

