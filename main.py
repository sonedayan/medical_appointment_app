from fastapi import FastAPI

app = FastAPI(
    title="Medical Appointment App",
    summary="An app that enables patients and doctors book appointments."
)


@app.get("/")
def home():
    return f"Welcome To Medical Appointment App"
