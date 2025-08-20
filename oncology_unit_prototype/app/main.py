from fastapi import FastAPI
from .database import Base, engine
from . import models
from .routers import patients, diagnoses, regimens, medications, inventory, appointments, prescriptions, visits

app = FastAPI(title="Oncology Unit Management API", version="0.1.0")

# Create tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(patients.router)
app.include_router(diagnoses.router)
app.include_router(regimens.router)
app.include_router(medications.router)
app.include_router(inventory.router)
app.include_router(appointments.router)
app.include_router(prescriptions.router)
app.include_router(visits.router)

@app.get("/health")
def health():
    return {"status": "ok"}
