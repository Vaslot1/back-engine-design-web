from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database
from formula.models import *

class Characteristic(database.Base):
    __tablename__ = 'characteristics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    engine_id = Column(Integer, ForeignKey('engines.id'), nullable=False)
    formulas = relationship("Formula", back_populates="characteristic")