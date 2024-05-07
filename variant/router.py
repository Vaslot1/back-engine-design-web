from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List

import variant.controller as controller
import schemas
from database import get_db

router = APIRouter()


@router.post("/variants/", response_model=schemas.Variant)
def create_engine(variant: schemas.VariantCreate, db: Session = Depends(get_db)):
    return controller.create_variant(db=db, variant=variant)


@router.get("/variants/", response_model=List[schemas.Variant])
def read_engines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    variants = controller.get_variants(db, skip=skip, limit=limit)
    return variants


@router.get("/variants/{id}", response_model=schemas.Variant)
def read_engine(id: int, db: Session = Depends(get_db)):
    db_variant = controller.get_variant(db, id=id)
    if db_variant is None:
        raise HTTPException(status_code=404, detail="variant not found")
    return db_variant
