from http import HTTPStatus

from fastapi import FastAPI

from fm_fastapi.routers import auth, users
from fm_fastapi.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
