from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from server.src import database
class Formula(database.Base):
    __tablename__ = 'formula'

    id = Column(Integer, primary_key=True, autoincrement=True)
    string_res = Column(String(50))
    number = Column(Integer)
    dim = Column(String(10))
    variables = relationship("Variable", secondary="variable_formula", back_populates="formula")
    characteristics = relationship("Characteristic", secondary="characteristic_formulas", back_populates="formula")
