from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database
from ref_tables.models import *
from variant.models import *

class Var_initial_data(database.Base):
    __tablename__ = 'vars_initial_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_name = Column(String(25), nullable=False)
    value = Column(Float)
    id_variant_user = Column(Integer, ForeignKey('variants_users.id'), nullable=False)
    variants_users = relationship("VariantUser",back_populates="vars_initial_data")
    # formulas = relationship("Formula", secondary="variable_formula", back_populates="variables")
    # users = relationship("User", secondary="variable_formula", back_populates="variables")