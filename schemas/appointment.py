from enum import Enum
from typing import List
from pydantic import BaseModel
from datetime import date

from schemas.doctor import Doctors, doctors
from schemas.patient import Patients, patients


class AppointmentStatus(Enum):
    pending = "Pending"
    completed = "Completed"


class Appointments(BaseModel):
    id: int
    patient: Patients
    doctor: Doctors
    date: date
    status: AppointmentStatus = AppointmentStatus.pending

class CreateAppointments(BaseModel):
    patient_id: int
    date: date


appointments: dict[int, Appointments] = {
    0:Appointments(id=0, patient=patients[0], doctor=doctors[0], date=date.today()),
    1:Appointments(id=1, patient=patients[1], doctor=doctors[1], date=date.today()),
}