from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
import var_initial_data.controller as controller
import schemas
from database import get_db

router = APIRouter()


@router.post("/api/varsinindata/", response_model=schemas.VarInitialData)
def create_varInitialData(varInitialData: schemas.VarInitialDataCreate, db: Session = Depends(get_db)):
    db_variable = controller.get_varInitialData_by_short_name(db, short_name=varInitialData.short_name)
    if db_variable:
        raise HTTPException(status_code=400, detail="short_name already registered")
    return controller.create_varInitialData(db=db, varInitialData=varInitialData)


@router.get("/api/varsinindata/", response_model=List[schemas.VarInitialData])
def read_variables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    varsInitialData = controller.get_varsInitialData(db, skip=skip, limit=limit)
    return varsInitialData


@router.get("/api/varsinindata/{id}", response_model=schemas.VarInitialData)
def read_variable(id: int, db: Session = Depends(get_db)):
    db_varInitialData = controller.get_varInitialData(db, id=id)
    if db_varInitialData is None:
        raise HTTPException(status_code=404, detail="var_initial_data not found")
    return db_varInitialData
