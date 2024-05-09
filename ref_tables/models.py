from sqlalchemy import Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship

import database

from variant.models import *
from characteristic.models import *
from var_initial_data.models import *
from formula.models import *


class VariantUser(database.Base):
    __tablename__ = 'variants_users'
    id = Column(Integer,primary_key=True, autoincrement=True)
    id_variant = Column(Integer, ForeignKey('variants.id'), nullable=False)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    variant = relationship("Variant", back_populates="variant_users")
    user = relationship("User", back_populates="variants_user")
    vars_initial_data = relationship("VarInitialData", back_populates="variants_users")