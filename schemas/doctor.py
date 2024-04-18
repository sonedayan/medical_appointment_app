from pydantic import BaseModel


class Doctors(BaseModel):
    id: str
    name: str
    specialization: str
    phone: str
    is_available: bool = True

