from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy.orm import deferred
import server.src.formula.schemas as formula



class CharacteristicBase(BaseModel):
    name: str
    engine_id: Optional[int] = None


class CharacteristicCreate(CharacteristicBase):
    name: str
    engine_id: Optional[int] = None


class Characteristic(CharacteristicBase):
    id: int
    formulas: List[formula.Formula] = []

    class Config:
        orm_mode = True