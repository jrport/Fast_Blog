from datetime import datetime
from typing import Annotated
from fastapi import Form
from pydantic import BaseModel, ConfigDict, Field, field_serializer


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
    title: str = Field(max_length=50, examples=["Generic Title"])
    content: str = Field(min_length=10, examples=[
        "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupicreated_att."
    ])


class PostIn(PostBase):
    title: str
    content: str


class PostOut(PostBase):
    id: int = Field()
    created_at: datetime = Field(serialization_alias='date')
    model_config = {"from_attributes": True, "populate_by_name": True}

    @field_serializer('created_at', when_used='json')
    def serialize(complete_date: datetime):
        return complete_date.date()
