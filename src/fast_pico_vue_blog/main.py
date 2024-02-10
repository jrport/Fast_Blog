import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_root():
    return ({"Hello": "World"})
