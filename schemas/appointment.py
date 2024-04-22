from pydantic import BaseModel
from datetime import date

from doctor import Doctors
from patient import Patients


class Appointments(BaseModel):
    id: int
    patient: Patients
    doctor: Doctors
    date: date
