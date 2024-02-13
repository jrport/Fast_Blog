import asyncio
from fastapi import Depends, FastAPI, Form, Query, HTTPException
from typing import Annotated, Any
from sqlalchemy import Sequence
from src.backend.models import Post
from src.backend.database import crud, database
from sqlalchemy.orm import Session
from . import schemas

app = FastAPI()

def get_session():
    session = database.local_session()
    try: 
        yield session
    finally:
        session.commit()
        session.close()

@app.get("/posts/"response_model=list[schemas.Post])
async def index(index: int = 1, session: Session = Depends(get_session)):
    posts = crud.get_all_posts(index, session)
    return posts

@app.get("/post/{post_id}", response_model=schemas.Post)
async def show_post(post_id: int, session: Session = Depends(get_session)):
    post = crud.get_post(post_id, session)
    if post:
        return post
    raise HTTPException(status_code=404, detail="No matching post") 

@app.post("/create_post/", response_model=schemas.Post)
async def create_post(post = schemas.PostCreate, session: Session = Depends(get_session)):
    crud.create_post(post=post, session=session)


@app.get("/login/")
async def login():
    return "get_rotated idiot"
