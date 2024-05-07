from sqlalchemy.orm import Session

import formula.models as models
import schemas


def get_formula(db: Session, id: int):
    return db.query(models.Formula).filter(models.Formula.id == id).first()


def get_formula_by_string_res(db: Session, string_res: str):
    return db.query(models.Formula).filter(models.Formula.string_res == string_res).first()


def get_formulas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Formula).offset(skip).limit(limit).all()


def create_formula(db: Session, formula: schemas.FormulaCreate):
    db_formula = models.Formula(string_res=formula.string_res, number=formula.number, dim=formula.dim)
    db.add(db_formula)
    db.commit()
    db.refresh(db_formula)
    return db_formula