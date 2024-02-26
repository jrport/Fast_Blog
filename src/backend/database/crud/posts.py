from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import Sequence, delete, select, update
from backend import models, schemas


async def get_all_posts(page_number: int, limit: int, session: Session):
    posts = select(models.Post).where(models.Post.id < page_number * 10).limit(limit=limit)
    posts = session.scalars(posts).all()
    return {k: v for k, v in enumerate(posts)}


async def get_post(post_id: int, session: Session) -> models.Post | None:
    post = select(models.Post).where(models.Post.id == post_id)
    return session.scalars(post).one_or_none()


async def create_post(title: str, content: str, session: Session) -> schemas.PostOut:
    new_post = models.Post(title=title, content=title, created_at=datetime.now())
    session.add(new_post)
    return new_post


async def update_post(post_id: int, title: str, content: str, session: Session) -> models.Post:
    updated_post = update(models.Post).where(models.Post.id == post_id).values(title=title, content=content)
    session.execute(updated_post)
    return await get_post(post_id, session)


async def delete_post(post_id: int, session: Session):
    to_delete_post = delete(models.Post).where(models.Post.id == post_id)
    session.execute(to_delete_post)
