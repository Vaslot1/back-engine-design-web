from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy.orm import deferred


class VariableBase(BaseModel):
    short_name: str


class VariableCreate(VariableBase):
    short_name: str


class Variable(VariableBase):
    id: int

    class Config:
        orm_mode = True