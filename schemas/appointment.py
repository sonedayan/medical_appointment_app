from pydantic import BaseModel
from datetime import date

from doctor import Doctors
from patient import Patient


class Appointments(BaseModel):
    id: int
    patient: Patient
    doctor: Doctors
    date: date
