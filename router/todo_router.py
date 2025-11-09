from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import Annotated
from ..db.bdconfig import get_session
from  ..models.fake_data import fake_data_db
from  ..models.todo_models import Todo

todo_router = APIRouter(prefix="/todo", tags=["todo"])

@todo_router.get("/")
async def get_todos():
    print("show all tasks")
    return fake_data_db


@todo_router.post("/")
async def post_todo(todo: Todo, db_session: Annotated[Session, Depends(get_session)]):
    db_session.add(todo)
    db_session.commit()
    db_session.refresh(todo)
    return {"created": todo}

