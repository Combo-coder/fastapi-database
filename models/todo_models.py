from sqlmodel import SQLModel, Field
from typing import Annotated


class Todo(SQLModel, table=True):
    id: Annotated[int, Field(default=None, primary_key=True)]
    task_name: Annotated[str, Field(index=True)]
    hour_to_achieve: Annotated[str, Field()]