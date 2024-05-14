from tokenize import String

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
import ref_tables.controller as controller
import schemas
from database import get_db

router = APIRouter()


@router.post("/api/variants_users/", response_model=schemas.VariantUser)
def create_variant_user(variant_user: schemas.VariantUserCreate, db: Session = Depends(get_db)):
    db_variant_user = controller.get_variant_user_by_id_user_variant(db, id_user=variant_user.id_user,
                                                               id_variant=variant_user.id_variant)
    if db_variant_user:
        raise HTTPException(status_code=400, detail=f"short_name already registered {variant_user.id_user} and {variant_user.id_variant} = {db_variant_user.id}")
    db_variant_user = controller.create_variant_user(db=db, variant_user=variant_user)
    db_formulas = controller.get_string_res_by_variant_id(db, id_variant=variant_user.id_variant)
    controller.create_vars_initial_data_from_formulas(db,db_formulas,db_variant_user.id)

    return db_variant_user


@router.get("/api/variants_users/", response_model=List[schemas.VariantUser])
def read_variants_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    engines = controller.get_variants_users(db, skip=skip, limit=limit)
    return engines


@router.get("/api/variants_users/{id}", response_model=schemas.VariantUser)
def read_variant_user(id: int, db: Session = Depends(get_db)):
    db_engine = controller.get_variant_user(db, id=id)
    if db_engine is None:
        raise HTTPException(status_code=404, detail="variant_user not found")
    return db_engine


@router.get("/api/variants_users/formulas/{id}", response_model=List[schemas.Formula])
def read_formulas_by_variant(id: int, db: Session = Depends(get_db)):
    db_formulas = controller.get_string_res_by_variant_id(db, id_variant=id)

    if db_formulas is None:
        raise HTTPException(status_code=404, detail="variant_user not found")
    return db_formulas
