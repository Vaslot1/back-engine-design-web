from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
import ref_tables.controller as controller
import schemas
from database import get_db

router = APIRouter()


@router.post("/variants_users/", response_model=schemas.VariantUser)
def create_variant_user(variant_user: schemas.VariantUserCreate, db: Session = Depends(get_db)):
    db_engine = controller.get_variant_user_by_id_user_variant(db, id_user=variant_user.id_user,
                                                               id_variant=variant_user.id_variant)
    if db_engine:
        raise HTTPException(status_code=400, detail="short_name already registered")
    return controller.create_variant_user(db=db, variant_user=variant_user)


@router.get("/variants_users/", response_model=List[schemas.VariantUser])
def read_variants_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    engines = controller.get_variants_users(db, skip=skip, limit=limit)
    return engines


@router.get("/variants_users/{id}", response_model=schemas.VariantUser)
def read_variant_user(id: int, db: Session = Depends(get_db)):
    db_engine = controller.get_variant_user(db, id=id)
    if db_engine is None:
        raise HTTPException(status_code=404, detail="variant_user not found")
    return db_engine
