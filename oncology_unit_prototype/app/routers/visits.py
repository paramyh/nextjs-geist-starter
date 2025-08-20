from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/visits", tags=["visits"])

@router.post("/", response_model=schemas.Visit)
def create_visit(payload: schemas.VisitCreate, db: Session = Depends(get_db)):
    v = models.Visit(**payload.dict())
    db.add(v)
    db.commit()
    db.refresh(v)
    return v

@router.get("/", response_model=List[schemas.Visit])
def list_visits(db: Session = Depends(get_db)):
    return db.query(models.Visit).all()
