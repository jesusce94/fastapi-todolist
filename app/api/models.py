from typing import List
from pydantic import BaseModel

class Todo(BaseModel):
    text: str
    tags: List[str]
