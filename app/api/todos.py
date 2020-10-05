from fastapi import APIRouter, Header, HTTPException
from typing import List

from app.api.models import Todo

fake_todos = [
    {
        'text': "Todo one",
        'tags': ["fastapi","python"]
    }
]

todos = APIRouter()

@todos.get('/todos')
async def index():
    return fake_todos

@todos.get('/todos/{id}')
async def get_todo(id: int):
    todos_length = len(fake_todos)
    if 0 <= id <= todos_length:
        return fake_todos[id]
    raise HTTPException(status_code=404, detail="Given id doesnt exist")

@todos.post('/todos', status_code=201)
async def add_todo(payload: Todo):
    todos = payload.dict()
    fake_todos.append(todos)
    return {'id': len(fake_todos)-1}

@todos.put('/todos/{id}')
async def modify_todo(id: int, payload: Todo):
    todos = payload.dict()
    todos_length = len(fake_todos)
    if 0 <= id <= todos_length:
        fake_todos[id] = todos
        return None
    raise HttpException(status_code = 404, detail="Todo with given id not found")

@todos.delete("todos/{id}")
async def delete_todo(id: int):
    todos_length = len(fake_todos)
    if 0 <= id <= todos_length:
        del fake_todos[id]
        return None
    raise HttpException(status_code=404, detail="Todo with given id does not exist")
