from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from .. import schemas
from ..dependencies import get_session
from ..database.crud import posts as crud

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    dependencies=[Depends(get_session)],
    responses={404: {"description": "Not found"}}
)

@router.get("/{page_number}", response_model=list[schemas.Post])
async def index(page_number: int = 1, limit: int = 10, session: Session = Depends(get_session)):
    posts = await crud.get_all_posts(page_number, limit, session)
    return posts

@router.post("/create_post/", response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, session: Session = Depends(get_session)):
    new_post = await crud.create_post(post, session)
    return new_post

@router.get("/read/{post_id}", response_model=schemas.Post)
async def show_post(post_id: int, session: Session = Depends(get_session)):
    post = await crud.get_post(post_id, session) 
    return post

@router.put("/edit/{post_id}", response_model=schemas.Post)
async def edit_post(post_id: int, post: schemas.Post, session: Session = Depends(get_session)):
    post = await crud.update_post(post_id, post, session)
    return post

@router.delete("/remove_post/{post_id}")
async def delete_post(post_id: int, session: Session = Depends(get_session)):
    post = await show_post(post_id, session)
    if post:
        await crud.delete_post(post_id, session)
        return "Sucessfully deleted"
    return HTTPException(status_code=404, detail=f"No post with matching id {post_id}")
