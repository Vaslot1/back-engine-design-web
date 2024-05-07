from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database
from ref_tables.models import *
from formula.models import *

class Variable(database.Base):
    __tablename__ = 'variables'

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_name = Column(String(25), nullable=False)
    # formulas = relationship("Formula", secondary="variable_formula", back_populates="variables")
    # users = relationship("User", secondary="variable_formula", back_populates="variables")