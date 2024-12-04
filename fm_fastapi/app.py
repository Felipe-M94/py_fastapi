from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fm_fastapi.routers import auth, todo, users
from fm_fastapi.templates import render_homepage

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todo.router)


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root():
    return HTMLResponse(content=render_homepage())
