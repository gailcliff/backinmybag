from ..asgi import application  # initialize db backend


from fastapi import FastAPI, Depends
from .models import User
from typing import Annotated

import dependencies


app = FastAPI()


@app.get('/')
def home():
    return 'Welcome Home!'


@app.post('/users', response_model_include={'id'})
def add_user(user: User) -> User:

    user.save()
    return user


@app.get('/users')
def get_all_users():
    return User.fetch_all()


@app.get('/users/lucky')
def get_lucky_users(lucky_winners: Annotated[list, Depends(dependencies.next_lucky_persons)]):
    return lucky_winners
