from sqlalchemy.orm import Session

import var_initial_data.models as models
import schemas


def get_varInitialData(db: Session, id: int):
    return db.query(models.VarInitialData).filter(models.VarInitialData.id == id).first()


def get_varInitialData_by_short_name(db: Session, short_name: str):
    return db.query(models.VarInitialData).filter(models.VarInitialData.short_name == short_name).first()


def get_varsInitialData(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VarInitialData).offset(skip).limit(limit).all()


def create_varInitialData(db: Session, varInitialData: schemas.VarInitialDataCreate):
    db_VarInitialData = models.VarInitialData(short_name=varInitialData.short_name, value=varInitialData.value,
                                          id_variant_user=varInitialData.id_variant_user)
    db.add(db_VarInitialData)
    db.commit()
    db.refresh(db_VarInitialData)
    return db_VarInitialData