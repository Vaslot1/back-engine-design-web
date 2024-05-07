from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database
from ref_tables.models import *

class Characteristic(database.Base):
    __tablename__ = 'characteristics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    engine = Column(Integer, ForeignKey('engines.id'))
    formula = relationship("Formula", secondary="characteristic_formulas", back_populates="characteristics")