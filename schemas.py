from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy.orm import deferred



#######################################################Engine
class EngineBase(BaseModel):
    name: str


class EngineCreate(EngineBase):
    name: str


class Engine(EngineBase):
    id: int
    # variants: List['Variant'] = deferred([])

    class Config:
        orm_mode = True
#######################################################User
class UserBase(BaseModel):
    full_name: str
    password: str
    user_group: Optional[str] = None
    role: Optional[str] = None


class UserCreate(UserBase):
    full_name: str
    password: str
    user_group: Optional[str] = None
    role: Optional[str] = None


class User(UserBase):
    id: int
    variants: List['Variant'] = deferred([])

    class Config:
        orm_mode = True

#######################################################Variant
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
    engine: Optional[int] = None


class Variant(VariantBase):
    id: int
    engine_obj: Optional[Engine] = None
    users: List[User] = []

    class Config:
        orm_mode = True
#######################################################Formula
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


#######################################################Variable
class VariableBase(BaseModel):
    short_name: str


class VariableCreate(VariableBase):
    short_name: str


class Variable(VariableBase):
    id: int

    class Config:
        orm_mode = True
#######################################################

class CharacteristicBase(BaseModel):
    name: str
    engine_id: Optional[int] = None


class CharacteristicCreate(CharacteristicBase):
    name: str
    engine_id: Optional[int] = None


class Characteristic(CharacteristicBase):
    id: int
    formulas: List[Formula] = []

    class Config:
        orm_mode = True
