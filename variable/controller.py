from sqlalchemy.orm import Session

import variable.models as models
import schemas


def get_variable(db: Session, id: int):
    return db.query(models.Variable).filter(models.Variable.id == id).first()


def get_variable_by_short_name(db: Session, short_name: str):
    return db.query(models.Variable).filter(models.Variable.short_name == short_name).first()


def get_variables(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Variable).offset(skip).limit(limit).all()


def create_variable(db: Session, variable: schemas.VariableCreate):
    db_variable = models.Variable(short_name=variable.short_name)
    db.add(db_variable)
    db.commit()
    db.refresh(db_variable)
    return db_variable