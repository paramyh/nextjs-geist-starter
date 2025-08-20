from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/prescriptions", tags=["prescriptions"])

@router.post("/", response_model=schemas.Prescription)
def create_rx(payload: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    rx = models.Prescription(
        patient_id=payload.patient_id,
        regimen_id=payload.regimen_id,
        date_prescribed=payload.date_prescribed,
        cycle_no=payload.cycle_no,
        notes=payload.notes
    )
    db.add(rx)
    db.commit()
    db.refresh(rx)

    for item in payload.items:
        it = models.PrescriptionItem(
            prescription_id=rx.id,
            medication_id=item.medication_id,
            dose=item.dose,
            frequency=item.frequency,
            route=item.route,
            notes=item.notes
        )
        db.add(it)
    db.commit()
    db.refresh(rx)
    return rx

@router.get("/", response_model=List[schemas.Prescription])
def list_rx(db: Session = Depends(get_db)):
    return db.query(models.Prescription).all()
