from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.post("/", response_model=schemas.Inventory)
def create_inventory(payload: schemas.InventoryCreate, db: Session = Depends(get_db)):
    inv = models.Inventory(**payload.dict())
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

@router.get("/", response_model=List[schemas.Inventory])
def list_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()
