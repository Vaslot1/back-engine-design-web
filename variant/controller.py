from sqlalchemy.orm import Session

import variant.models as models
import schemas


def get_variant(db: Session, id: int):
    return db.query(models.Variant).filter(models.Variant.id == id).first()


def get_variants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Variant).offset(skip).limit(limit).all()


def create_variant(db: Session, variant: schemas.VariantCreate):
    db_variant= models.Variant(voltage=variant.voltage, power=variant.power, cnt_pole=variant.cnt_pole,
                               solved=variant.solved, slide=variant.slide, class_hr=variant.class_hr,
                               engine=variant.engine)
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant