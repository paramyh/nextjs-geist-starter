from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("/", response_model=schemas.Appointment)
def create_appt(payload: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    a = models.Appointment(**payload.dict())
    db.add(a)
    db.commit()
    db.refresh(a)
    return a

@router.get("/", response_model=List[schemas.Appointment])
def list_appts(db: Session = Depends(get_db)):
    return db.query(models.Appointment).all()
