from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/medications", tags=["medications"])

@router.post("/", response_model=schemas.Medication)
def create_med(payload: schemas.MedicationCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Medication).filter(models.Medication.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Medication already exists")
    m = models.Medication(**payload.dict())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

@router.get("/", response_model=List[schemas.Medication])
def list_meds(db: Session = Depends(get_db)):
    return db.query(models.Medication).all()
