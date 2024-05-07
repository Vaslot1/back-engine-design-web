from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
import engine.controller as controller
import schemas
from database import get_db

router = APIRouter()


@router.post("/engines/", response_model=schemas.Engine)
def create_engine(engine: schemas.EngineCreate, db: Session = Depends(get_db)):
    db_engine = controller.get_engine_by_name(db, name=engine.name)
    if db_engine:
        raise HTTPException(status_code=400, detail="short_name already registered")
    return controller.create_user(db=db, engine=engine)


@router.get("/engines/", response_model=List[schemas.Engine])
def read_engines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    engines = controller.get_engines(db, skip=skip, limit=limit)
    return engines


@router.get("/engines/{id}", response_model=schemas.Engine)
def read_engine(id: int, db: Session = Depends(get_db)):
    db_engine = controller.get_engine(db, id=id)
    if db_engine is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_engine
