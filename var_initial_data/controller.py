from sqlalchemy.orm import Session

import var_initial_data.models as models
import schemas


def get_varInitialData(db: Session, id: int):
    return db.query(models.Var_initial_data).filter(models.Var_initial_data.id == id).first()


def get_varInitialData_by_short_name(db: Session, short_name: str):
    return db.query(models.Var_initial_data).filter(models.Var_initial_data.short_name == short_name).first()


def get_varsInitialData(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Var_initial_data).offset(skip).limit(limit).all()


def create_varInitialData(db: Session, varInitialData: schemas.VarInitialDataCreate):
    db_VarInitialData = models.Var_initial_data(short_name=varInitialData.short_name, value=varInitialData.value,
                                          id_variant_user=varInitialData.id_variant_user)
    db.add(db_VarInitialData)
    db.commit()
    db.refresh(db_VarInitialData)
    return db_VarInitialData