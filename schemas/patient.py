from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "Male"
    female = "Female"


class Patient(BaseModel):
    id: str
    name: str
    age: int
    gender: Gender
    weight: int
    height: float
    phone: str
