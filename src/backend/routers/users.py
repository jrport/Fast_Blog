from fastapi import APIRouter, Depends

from backend import schemas

from backend.dependencies import get_session

router = APIRouter(
    prefix="/users",
    dependencies=[Depends(get_session)],
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

@router.get("/{user_id}", response_model=list[schemas.User])
async def index(user_id: int, session: Session = Depends(get_session)):
    comments = await get_comments_by_user(user_id, session)
    pass
