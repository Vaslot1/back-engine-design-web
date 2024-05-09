from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database
from ref_tables.models import *


class User(database.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(150), nullable=False)
    password = Column(String, nullable=False)
    user_group = Column(String(20))
    role = Column(String(10))
    variants_user = relationship("VariantUser", back_populates="user")
