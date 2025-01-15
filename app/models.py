from sqlalchemy import Column, Integer, String
from .database import Base

class Greetings(Base):
    __tablename__ = 'greetings'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)

    