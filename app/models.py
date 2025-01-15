from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, VARCHAR, Boolean
from sqlalchemy.sql import func
from .database import Base
from sqlalchemy.orm import relationship

# class Greetings(Base):
#     __tablename__ = 'greetings'

#     id = Column(Integer, primary_key=True, index=True)
#     message = Column(String)


class Users(Base):
    id = Column(Integer, primary_key=True, index= True)
    username = Column(String,nullable=False, unique=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(VARCHAR)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),onupdate=func.now())

class Posts(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("Users.id"))
    category = Column(VARCHAR)
    status = Column(VARCHAR)
    views = Column(Integer)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),onupdate=func.now())

class Tags(Base):
    id = Column(Integer,primary_key=True)
    name = Column(VARCHAR, unique=True, nullable=False)

Post_Tags = Table(
    'Post_Tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('Posts.id')),
    Column('tags_id', Integer, ForeignKey('Tags.id'))
)

class Comments(Base):
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    author_id = Column(Integer, ForeignKey('Users.id'))
    parent_id = Column(Integer,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Likes_Dislikes(Base):
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    user_id = Column(Integer, ForeignKey('Users.id')) 
    is_like = Column(Boolean)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    