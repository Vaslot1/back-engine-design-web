from typing import List, Optional

from pydantic import BaseModel

from sqlalchemy.orm import deferred


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

    class Config:
        orm_mode = True