from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import variable.controller as controller
import schemas
from database import get_db

router = APIRouter()


@router.post("/variables/", response_model=schemas.Variable)
def create_variable(variable: schemas.VariableCreate, db: Session = Depends(get_db)):
    db_variable = controller.get_variable_by_short_name(db, short_name=variable.short_name)
    if db_variable:
        raise HTTPException(status_code=400, detail="short_name already registered")
    return controller.create_variable(db=db, variable=variable)


@router.get("/variables/", response_model=list[schemas.Variable])
def read_variables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    variables = controller.get_variables(db, skip=skip, limit=limit)
    return variables


@router.get("/variables/{id}", response_model=schemas.Variable)
def read_variable(id: int, db: Session = Depends(get_db)):
    db_variable = controller.get_variable(db, id=id)
    if db_variable is None:
        raise HTTPException(status_code=404, detail="variable not found")
    return db_variable
