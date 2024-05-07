from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy.orm import deferred
import server.src.engine.schemas as engine
import server.src.user.schemas as user


class VariantBase(BaseModel):
    voltage: Optional[float] = None
    power: Optional[float] = None
    cnt_pole: Optional[int] = None
    solved: Optional[bool] = None
    slide: Optional[float] = None
    class_hr: Optional[str] = None
    engine_id: Optional[int] = None


class VariantCreate(VariantBase):
    voltage: Optional[float] = None
    power: Optional[float] = None
    cnt_pole: Optional[int] = None
    solved: Optional[bool] = None
    slide: Optional[float] = None
    class_hr: Optional[str] = None
    engine_id: Optional[int] = None


class Variant(VariantBase):
    id: int
    engine: Optional[engine.Engine] = None
    users: List[user.User] = []

    class Config:
        orm_mode = True