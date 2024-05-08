from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database
from ref_tables.models import *
from characteristic.models import *

class Formula(database.Base):
    __tablename__ = 'formula'

    id = Column(Integer, primary_key=True, autoincrement=True)
    string_res = Column(String(50))
    number = Column(Integer)
    dim = Column(String(10))
    id_char = Column(Integer, ForeignKey('characteristics.id'), nullable=False)
    # variables = relationship("Variable", secondary="variable_formula", back_populates="formula")
    characteristic = relationship("Characteristic", back_populates="formulas")
