from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from .routers import posts
from .dependencies import get_session
from . import schemas, utils
from .database.crud import posts as crud

app = FastAPI(dependencies=[Depends(get_session)])

################# ROUTERS #######################################################################

@app.get("/", response_model=dict[int, schemas.Post])
async def index(page_number: int = 1, limit: int = 10, session: Session = Depends(get_session)):
    posts = await crud.get_all_posts(page_number, limit, session)
    return posts

app.include_router(posts.router)
app.include_router(utils.router)

@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
   return PlainTextResponse(str({"details": [error["msg"] for error in exc.errors()]}))

################## CORS #########################################################################

origins = [
   "http://localhost:5173/",
   "http://localhost:8080/",
   "http://localhost:8000/",
   "http://localhost/"
]

app.add_middleware(
   CORSMiddleware,
   allow_origins=['*'],
   allow_methods=['GET'],
   expose_headers=['*']
)
   
