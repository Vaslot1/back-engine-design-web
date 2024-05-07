from sqlalchemy import Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship

import database

from variant.models import *
from characteristic.models import *
from variable.models import *
from formula.models import *

class CharacteristicFormula(database.Base):
    __tablename__ = 'characteristic_formulas'

    id_characteristic = Column(Integer, ForeignKey('characteristics.id'), primary_key=True)
    id_formula = Column(Integer, ForeignKey('formula.id'), primary_key=True)
    characteristic = relationship("Characteristic", backref="related_formulas")
    formula = relationship("Formula", backref="related_characteristics")

class VariableFormula(database.Base):
    __tablename__ = 'variable_formula'

    id_variable = Column(Integer, ForeignKey('variables.id'), primary_key=True)
    id_formula = Column(Integer, ForeignKey('formulas.id'), primary_key=True)
    # user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    # value = Column(Float)
    # variable = relationship("Variable", backref="formulas")
    # formula = relationship("Formula", backref="variables")
    # user = relationship("User", backref="users")
class VariantUser(database.Base):
    __tablename__ = 'variants_users'

    id_variant = Column(Integer, ForeignKey('variants.id'), primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    variant = relationship("Variant", backref="related_users")
    user = relationship("User", backref="related_variants")