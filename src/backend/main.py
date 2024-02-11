import asyncio
from fastapi import FastAPI, Form, Query
from typing import Annotated
# from pydantic import 

app = FastAPI()

@app.get("/")
async def get_root(name: Annotated[ str, Query(max_length=30) ] = None):
    if name:
        return ({"Hello": f"bobão {name}"})
    return ("Quem é vc?")
