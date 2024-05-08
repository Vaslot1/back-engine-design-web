from sqlalchemy.orm import Session

import characteristic.models as models
import schemas


def get_characteristic(db: Session, id: int):
    return db.query(models.Characteristic).filter(models.Characteristic.id == id).first()


def get_characteristic_by_name(db: Session, name: str):
    return db.query(models.Characteristic).filter(models.Characteristic.name == name).first()


def get_characteristics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Characteristic).offset(skip).limit(limit).all()


def create_characteristic(db: Session, characteristic: schemas.CharacteristicCreate):
    db_characteristic = models.Characteristic(name=characteristic.name, engine_id=characteristic.engine_id)
    db.add(db_characteristic)
    db.commit()
    db.refresh(db_characteristic)
    return db_characteristic