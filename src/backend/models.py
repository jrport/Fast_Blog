from typing import Text
from sqlalchemy import Column, DateTime, Integer, String, Text
from .database.database import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime)
