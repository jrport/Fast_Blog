from datetime import datetime
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    comments: list[int]
    created_at: datetime = Field(default=datetime.now(), examples=[datetime.now()])

class UserCreate(BaseModel):
    pass

class User(BaseModel):
    name: str = Field(min_length=5, examples=["deTonaTor123", "fenix8071"])
    comments: list[int]
    created_at: datetime
    model_config = {"from_attributes": True}

class PostBase(BaseModel):
    title: str
    content: str
    created_at: datetime = Field(default=datetime.now(), examples=[datetime.now()])
    
class PostCreate(PostBase):
    pass

class Post(PostBase):
    title: str = Field(max_length=50, examples=["Generic Title"])
    content: str = Field(min_length=10, examples=[
        "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat."
                                                  ])
    created_at: datetime 
    model_config = {"from_attributes": True} 
