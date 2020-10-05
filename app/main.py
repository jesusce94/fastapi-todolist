from fastapi import FastAPI, APIRouter
from app.api.models import Todo
from enum import Enum
from pydantic import BaseModel
from typing import Optional
from app.api.todos import todos



app = FastAPI()


app.include_router(todos)
