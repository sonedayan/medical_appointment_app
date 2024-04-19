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

# class PatientsCreate(BaseModel):
#     name: str
#     age: int
#     gender: Gender
#     weight: int
#     height: float
#     phone: str


patients: dict[int, Patients] = {
    0: Patients(
        id=0,
        name="Mah Ange Carine",
        age=25,
        gender=Gender.female,
        weight=70,
        height=1.75,
        phone="0700000000",
    ),
    1: Patients(
        id=1,
        name="Dayan Sone",
        age=25,
        gender=Gender.male,
        weight=70,
        height=1.75,
        phone="0700000000",
    ),
    2:Patients(
        id=2,
        name="Mewoulou Le Roy Loic",
        age=25,
        gender=Gender.male,
        weight=70,
        height=1.75,
        phone="0700000000",
    )
}