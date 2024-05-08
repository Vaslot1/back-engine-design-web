from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy.orm import deferred



#######################################################Engine


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
    engine_obj: 'Engine'
    users: List[User] = []
    vars_initial_data: List['VarInitialData'] = None

    class Config:
        orm_mode = True
#######################################################Formula
class FormulaBase(BaseModel):
    string_res: Optional[str] = None
    number: Optional[int] = None
    dim: Optional[str] = None
    id_char:Optional[int] = None


class FormulaCreate(FormulaBase):
    string_res: Optional[str] = None
    number: Optional[int] = None
    dim: Optional[str] = None
    id_char: int


class Formula(FormulaBase):
    id: int
    # variables: List['Variable'] = deferred([])

    class Config:
        orm_mode = True


#######################################################Variable
class VarInitialDataBase(BaseModel):
    short_name: str
    value: float
    id_variant_user: int


class VarInitialDataCreate(VarInitialDataBase):
    short_name: str
    value: float
    id_variant_user: int


class VarInitialData(VarInitialDataBase):
    id: int
    value: float
    id_variant_user: int


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
    engine_id: int
    formulas: List[Formula] = []

    class Config:
        orm_mode = True

class EngineBase(BaseModel):
    name: str


class EngineCreate(EngineBase):
    name: str


class Engine(EngineBase):
    id: int
    characteristics: List[Characteristic] = []

    class Config:
        orm_mode = True

class VariantUserBase(BaseModel):
    # id: Optional[int]
    id_user:int
    id_variant:int


class VariantUserCreate(VariantUserBase):
    # id: Optional[int]
    id_user: int
    id_variant: int


class VariantUser(VariantUserBase):
    id: Optional[int]
    id_user: int
    id_variant: int
    vars_initial_data: List[VarInitialData] = []

    class Config:
        orm_mode = True

