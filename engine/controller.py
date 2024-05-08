from sqlalchemy.orm import Session

import engine.models as models
import schemas


def get_engine(db: Session, id: int):
    return db.query(models.Engine).filter(models.Engine.id == id).first()


def get_engine_by_name(db: Session, name: str):
    return db.query(models.Engine).filter(models.Engine.name == name).first()


def get_engines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Engine).offset(skip).limit(limit).all()


def create_engine(db: Session, engine: schemas.EngineCreate):
    db_engine = models.Engine(name=engine.name)
    db.add(db_engine)
    db.commit()
    db.refresh(db_engine)
    return db_engine