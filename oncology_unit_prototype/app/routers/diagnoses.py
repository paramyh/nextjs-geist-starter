from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/diagnoses", tags=["diagnoses"])

@router.post("/", response_model=schemas.Diagnosis)
def create_diagnosis(payload: schemas.DiagnosisCreate, db: Session = Depends(get_db)):
    d = models.Diagnosis(**payload.dict())
    db.add(d)
    db.commit()
    db.refresh(d)
    return d

@router.get("/", response_model=List[schemas.Diagnosis])
def list_diagnoses(db: Session = Depends(get_db)):
    return db.query(models.Diagnosis).all()
