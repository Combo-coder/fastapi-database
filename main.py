from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db.bdconfig import create_tables
from .router import todo_router

@asynccontextmanager
async def app_lifetime(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=app_lifetime)
app.include_router(todo_router.todo_router)