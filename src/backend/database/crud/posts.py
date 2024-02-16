from sqlalchemy.orm import Session
from sqlalchemy import Sequence, delete, select, update
from ... import models, schemas

async def get_all_posts(page_number: int, limit: int, session: Session):
    posts = select(models.Post).where(models.Post.id < page_number*10).limit(limit=limit)
    posts = session.scalars(posts).all() 
    return {k:v for k,v in enumerate(posts)}
async def get_post(post_id: int, session: Session) -> models.Post | None:
    post = select(models.Post).where(models.Post.id == post_id)
    return session.scalars(post).one_or_none()
    
async def create_post(post: schemas.PostCreate, session: Session) -> models.Post:
    new_post = models.Post(title=post.title, content=post.content, created_at=post.created_at)
    session.add(new_post)
    return new_post

async def update_post(post_id: int, post: schemas.Post, session: Session) -> models.Post:
    update_post = update(models.Post).where(models.Post.id == post_id).values(title=post.title, content=post.content)
    session.execute(update_post)
    return await get_post(post_id, session)

async def delete_post(post_id: int, session: Session):
    delete_post = delete(models.Post).where(models.Post.id == post_id)
    session.execute(delete_post)
