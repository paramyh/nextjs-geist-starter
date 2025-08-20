from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/", response_model=schemas.Patient)
def create_patient(payload: schemas.PatientCreate, db: Session = Depends(get_db)):
    # enforce uniqueness on hospital_id
    existing = db.query(models.Patient).filter(models.Patient.hospital_id == payload.hospital_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Hospital ID already exists")
    patient = models.Patient(**payload.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@router.get("/", response_model=List[schemas.Patient])
def list_patients(db: Session = Depends(get_db)):
    return db.query(models.Patient).all()

@router.get("/{patient_id}", response_model=schemas.Patient)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    p = db.query(models.Patient).get(patient_id)
    if not p:
        raise HTTPException(status_code=404, detail="Patient not found")
    return p

@router.put("/{patient_id}", response_model=schemas.Patient)
def update_patient(patient_id: int, payload: schemas.PatientCreate, db: Session = Depends(get_db)):
    p = db.query(models.Patient).get(patient_id)
    if not p:
        raise HTTPException(status_code=404, detail="Patient not found")
    for k, v in payload.dict().items():
        setattr(p, k, v)
    db.commit()
    db.refresh(p)
    return p

@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    p = db.query(models.Patient).get(patient_id)
    if not p:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(p)
    db.commit()
    return {"ok": True}
