from typing import Any
from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session
from src.backend.models import Post
from src.backend import schemas

def get_all_posts(index: int, session: Session):
    posts = select(Post).where(Post.id < index*10)
    return session.scalars(posts).all()

def get_post(post_id: int, session: Session):
    post = select(Post).where(Post.id == post_id)
    return session.scalars(post).one_or_none()
    
def create_post(post: schemas.PostCreate, session: Session):
    new_post = Post(title=post.title, content=post.content)
    session.add(new_post)
    return new_post
