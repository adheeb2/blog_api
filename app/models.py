from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, VARCHAR, Boolean
from sqlalchemy.sql import func
from .database import Base
from sqlalchemy.orm import relationship

# class Greetings(Base):
#     __tablename__ = 'greetings'

#     id = Column(Integer, primary_key=True, index=True)
#     message = Column(String)



class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index= True)
    username = Column(String,nullable=False, unique=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(VARCHAR, default="viewer")
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),onupdate=func.now())
    posts = relationship("Post", back_populates='author')


post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Post(Base):

    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    category = Column(VARCHAR)
    status = Column(VARCHAR)
    views = Column(Integer)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),onupdate=func.now())
    author = relationship("User", back_populates='posts')
    tags = relationship("Tag", secondary=post_tags, back_populates='posts')



class Tag(Base):
    __tablename__= 'tags'
    id = Column(Integer,primary_key=True)
    name = Column(VARCHAR, unique=True, nullable=False, index=True)
    posts = relationship('Post',secondary=post_tags ,back_populates='tags')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    parent_id = Column(Integer,ForeignKey('comments.id'),nullable=True,)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    parent = relationship("Comment", backref="children", remote_side=[id])

class Connection(Base):
    __tablename__ = 'connections'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False) 
    is_like = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
