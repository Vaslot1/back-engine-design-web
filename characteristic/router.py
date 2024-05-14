from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
import characteristic.controller as controller
import schemas
from database import get_db

router = APIRouter()


@router.post("/api/characteristics/", response_model=schemas.Characteristic)
def create_characteristic(characteristic: schemas.CharacteristicCreate, db: Session = Depends(get_db)):
    db_characteristic = controller.get_characteristic_by_name(db, name=characteristic.name)
    if db_characteristic:
        raise HTTPException(status_code=400, detail="name already registered")
    return controller.create_characteristic(db=db, characteristic=characteristic)


@router.get("/api/characteristics/", response_model=List[schemas.Characteristic])
def read_characteristics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    engines = controller.get_characteristics(db, skip=skip, limit=limit)
    return engines


@router.get("/api/characteristics/{id}", response_model=schemas.Characteristic)
def read_characteristic(id: int, db: Session = Depends(get_db)):
    db_characteristic = controller.get_characteristic(db, id=id)
    if db_characteristic is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_characteristic
