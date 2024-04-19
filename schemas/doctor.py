from typing import List
from pydantic import BaseModel


class Doctors(BaseModel):
    id: str
    name: str
    specialization: str
    phone: str
    is_available: bool = True

doctors: dict[int, Doctors] = {
    0:Doctors(id="1", name="Dr. Nkeangnyi Divine", specialization="Neurologist", phone="0712345678", is_available= True),
    1:Doctors(id="2", name="Dr. Akwo Ashley", specialization="Cardiologist", phone="0712345678", is_available= False),
    2:Doctors(id="3", name="Dr. Nkemnang Kenne", specialization="Botanist", phone="0712345678", is_available=False),
}