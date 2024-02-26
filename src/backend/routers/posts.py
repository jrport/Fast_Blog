from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from backend import schemas
from backend.dependencies import get_session
from backend.database.crud import posts as crud

router = APIRouter(
    tags=["posts"],
    dependencies=[Depends(get_session)],
    responses={404: {"description": "Not found"}}
)

@router.post("/create_post", status_code=201)
async def create_post(
    title: str,
    content: str,
    session: Session = Depends(get_session)
    ):
    new_post = await crud.create_post(title, content, session)
    return new_post


@router.get("/posts/read/{post_id}", response_model=schemas.PostOut)
async def show_post(post_id: int, session: Session = Depends(get_session)):
    post = await crud.get_post(post_id, session)
    if post:
        return post
    raise HTTPException(status_code=404, detail=f"No post with matching id: {post_id}")

@router.put("/edit/{post_id}", response_model=schemas.PostOut)
async def edit_post(
    post_id: int,
    title: Annotated[str, Form(max_length=40)] = None,
    content: Annotated[str, Form(min_length=40)] = None,
    session: Session = Depends(get_session)
    ) -> schemas.PostOut:
    post = await crud.update_post(post_id, post, session)
    return post


@router.delete("/remove_post/{post_id}", status_code=204)
async def delete_post(post_id: int, session: Session = Depends(get_session)):
    post = await show_post(post_id, session)
    if post:
        await crud.delete_post(post_id, session)
        return "Sucessfully deleted"
    return HTTPException(status_code=404, detail=f"No post with matching id {post_id}")
