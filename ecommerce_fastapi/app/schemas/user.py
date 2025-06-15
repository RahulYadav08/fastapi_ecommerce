from pydantic import BaseModel, EmailStr
from typing import Optional

#Shared properties
class UserBase(BaseModel):
    username: str
    email: EmailStr


#Used for creation
class UserCreate(UserBase):
    password: str


#Used for reading(returned to frontend)
class UserOut(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True #Required to use SQLAlchemy objects directly