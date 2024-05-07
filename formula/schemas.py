from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy.orm import deferred


class FormulaBase(BaseModel):
    string_res: Optional[str] = None
    number: Optional[int] = None
    dim: Optional[str] = None


class FormulaCreate(FormulaBase):
    string_res: Optional[str] = None
    number: Optional[int] = None
    dim: Optional[str] = None


class Formula(FormulaBase):
    id: int

    class Config:
        orm_mode = True