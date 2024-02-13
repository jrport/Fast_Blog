from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post():
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
