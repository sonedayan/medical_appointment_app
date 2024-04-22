from fastapi import FastAPI
from router.patient_route import patient_router
from router.doctor_route import doctor_router
from router.appointment_route import appointment_router
app = FastAPI(
    title="Medical Appointment App",
    summary="An app that enables patients and doctors book appointments."
)

app.include_router(router=patient_router, prefix="/patients", tags=["Patients"])
app.include_router(router=doctor_router, prefix="/doctors", tags=["Doctors"])
app.include_router(router=appointment_router, prefix="/appointments", tags=["Appointments"])

@app.get("/")
def home():
    return f"Welcome To Medical Appointment App"
