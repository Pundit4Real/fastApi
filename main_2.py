from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID

from typing import Optional


app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field()
    author: str = Field(min_length=1)
    description: Optional(str) = Field(title="Description of the book",
                             min_length=1, 
                             max_length=50)
    rating: int


Books= []

@app.get('/')
async def read_all_books():
    return Books


@app.post('/')
async def create_book(book:Book):
    Books.append(book)
    return book