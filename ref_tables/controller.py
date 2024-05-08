from sqlalchemy.orm import Session

import ref_tables.models as models
import schemas


def get_variant_user(db: Session, id: int):
    return db.query(models.VariantUser).filter(models.VariantUser.id == id).first()


def get_variant_user_by_id_user_variant(db: Session, id_user: int, id_variant: int):
    return db.query(models.VariantUser).filter(models.VariantUser.id_user == id_user
                                               and models.VariantUser.id_variant == id_variant).first()


def get_variants_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VariantUser).offset(skip).limit(limit).all()


def create_variant_user(db: Session, variant_user: schemas.VariantUserCreate):
    db_variant_user = models.VariantUser(id_user=variant_user.id_user,id_variant=variant_user.id_variant)
    db.add(db_variant_user)
    db.commit()
    db.refresh(db_variant_user)
    return db_variant_user