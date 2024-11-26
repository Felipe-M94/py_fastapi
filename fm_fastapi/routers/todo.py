from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fm_fastapi.database import get_session
from fm_fastapi.models import Todo, User
from fm_fastapi.schemas import TodoPublic, TodoSchema
from fm_fastapi.security import get_current_user

router = APIRouter(prefix="/todos", tags=["todos"])

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post("/", response_model=TodoPublic)
def create_todo(todo: TodoSchema, session: Session, user: CurrentUser):  # type: ignore
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo
