from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship

import database

from engine.models import *
class Variant(database.Base):
    __tablename__ = 'variants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    voltage = Column(Float)
    power = Column(Float)
    cnt_pole = Column(Integer)
    solved = Column(Boolean)
    slide = Column(Float)
    class_hr = Column(String(1))
    engine = Column(Integer, ForeignKey('engines.id'))
    engine_obj = relationship("Engine", back_populates="variants")
    users = relationship("User", secondary="variants_users", back_populates="variants")