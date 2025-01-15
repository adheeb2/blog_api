from pydantic import BaseModel
from typing import Optional

class GreetingBase(BaseModel):
    message: str

class GreetingCreate(GreetingBase):
    pass
class Greeting(GreetingBase):
    id : int

#User
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password : str

class UserUpdate(UserBase):
    is_active = Optional[bool] = None

class UserInDB(UserBase):
    id : int 
    is_active: bool


