from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/regimens", tags=["regimens"])

@router.post("/", response_model=schemas.Regimen)
def create_regimen(payload: schemas.RegimenCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Regimen).filter(models.Regimen.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Regimen already exists")
    r = models.Regimen(**payload.dict())
    db.add(r)
    db.commit()
    db.refresh(r)
    return r

@router.get("/", response_model=List[schemas.Regimen])
def list_regimens(db: Session = Depends(get_db)):
    return db.query(models.Regimen).all()
