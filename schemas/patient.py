#from typing import List
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "Male"
    female = "Female"


class Patients(BaseModel):
    id: int
    name: str
    age: int
    gender: Gender
    weight: int
    height: float
    phone: str

class PatientsCreateAndEdit(BaseModel):
    name: str
    age: int
    gender: Gender
    weight: int
    height: float
    phone: str


patients: dict[int, Patients] = {
    0: Patients(
        id=0, name="Mah Ange Carine", age=20, gender="Female", weight=70, height=1.7, phone="237625464852"
    ),
    1: Patients(
        id=1, name="Mewoulou Loic Le Roy", age=22, gender="Male", weight=65, height=1.5, phone="237674895623"
    ),
    2: Patients(
        id=2, name="Nadine Hadjeu", age=28, gender="Female", weight=54, height=1.2, phone="237656234587"
    ),
}