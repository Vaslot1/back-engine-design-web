import re
from typing import List

from sqlalchemy.orm import Session

import ref_tables.models as models

from formula.models import Formula
from variant.models import Variant
from characteristic.models import Characteristic
from var_initial_data.models import VarInitialData
import schemas


def get_variant_user(db: Session, id: int):
    return db.query(models.VariantUser).filter(models.VariantUser.id == id).first()


def get_variant_user_by_id_user_variant(db: Session, id_user: int, id_variant: int):
    return (db.query(models.VariantUser).filter(models.VariantUser.id_user == id_user)
            .filter(models.VariantUser.id_variant == id_variant).first())


def get_variants_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VariantUser).offset(skip).limit(limit).all()


def create_variant_user(db: Session, variant_user: schemas.VariantUserCreate):
    db_variant_user = models.VariantUser(id_user=variant_user.id_user,id_variant=variant_user.id_variant)
    db.add(db_variant_user)
    db.commit()
    db.refresh(db_variant_user)
    return db_variant_user

def get_formulas_by_variant_id(db: Session):
    return db.query(models.VariantUser).all()



def get_string_res_by_variant_id(db: Session, id_variant: int):
    return (
        db.query(Formula)
        .join(Characteristic)
        .filter(Characteristic.engine_id == Variant.engine_id)
        .filter(Characteristic.formulas.any(Formula.id_char == Characteristic.id))
        .filter(Variant.id == id_variant)
        .all()
    )

def create_vars_initial_data_from_formulas(db: Session, formulas: List[Formula],id_variant_user: int):
    def extract_variables_from_expression(expression):
        regex = r"[a-zA-Zа-яА-Я_'()][a-zA-Zа-яА-Я0-9_'()]*"
        variables = re.findall(regex, expression)
        func = variables[0]
        equals = set(var for index, var in enumerate(variables) if index != 0)
        return func, equals

    calculated_variables = set()
    initial_variables = set()

    for item in formulas:
        string_res = item.string_res
        func, equals = extract_variables_from_expression(string_res)
        calculated_variables.add(func)
        initial_variables.update(equals - calculated_variables)

    for var in initial_variables:
        db_VarInitialData = VarInitialData(short_name=var, value=None,
                                                    id_variant_user=id_variant_user)
        db.add(db_VarInitialData)
        db.commit()
        db.refresh(db_VarInitialData)
