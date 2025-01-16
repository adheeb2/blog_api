from sqlalchemy import VARCHAR
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

#Post

class PostCreate(BaseModel):
    title: str
    content: str
    status : str

class PostResponse(BaseModel):
    id : int
    title : str
    content: str
    views : int
    status : str
    created_at : datetime
    updated_at : Optional[datetime] 

class PostUpdate(PostCreate):
    status : str
    views : int
