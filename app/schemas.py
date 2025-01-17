from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from app.models import Role

#Post

class PostCreate(BaseModel):
    title: str
    content: str
    status : Optional[str] = None

class PostResponse(BaseModel):
    id : int
    title : str
    content: str
    views : int
    status : str
    created_at : datetime
    updated_at : Optional[datetime] = None

class PostUpdate(PostCreate):
    status : str
    views : int

class UserBase(BaseModel):
    username : str
    email : str

class PostResponseWithAuthor(PostResponse):
    author : UserBase
#User



class UserCreate(BaseModel):
    username : str
    email : str
    password : str
    role : Optional[Role] = None

    class Config:
        use_enum_values = True

class UserResponse(BaseModel):
    id : int
    username : str
    email : str
    role : str
    created_at : datetime
    updated_at : Optional[datetime] = None

class UserUpdate(BaseModel):
    username: str
    role : str

class UserLogin(BaseModel):
    email : str
    password : str

