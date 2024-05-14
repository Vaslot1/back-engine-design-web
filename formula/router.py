from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List

import formula.controller as controller
import schemas

from database import get_db

router = APIRouter()


@router.post("/api/formulas/", response_model=schemas.Formula)
def create_formula(formula: schemas.FormulaCreate, db: Session = Depends(get_db)):
    db_formula = controller.get_formula_by_string_res(db, string_res=formula.string_res)
    if db_formula:
        raise HTTPException(status_code=400, detail="string_res already registered")
    return controller.create_formula(db=db, formula=formula)


@router.get("/api/formulas/", response_model=List[schemas.Formula])
def read_formulas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    formulas = controller.get_formulas(db, skip=skip, limit=limit)
    return formulas


@router.get("/api/formulas/{id}", response_model=schemas.Formula)
def read_formula(id: int, db: Session = Depends(get_db)):
    db_formula = controller.get_formula(db, id=id)
    if db_formula is None:
        raise HTTPException(status_code=404, detail="formula not found")
    return db_formula
