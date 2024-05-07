from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database
from ref_tables.models import *

class Engine(database.Base):
    __tablename__ = 'engines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    variants = relationship("Variant", back_populates="engine_obj")