from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy.orm import deferred

import server.src.variant.schemas as variant



class EngineBase(BaseModel):
    name: str


class EngineCreate(EngineBase):
    name: str


class Engine(EngineBase):
    id: int
    variants: List[variant.Variant] = []

    class Config:
        orm_mode = True