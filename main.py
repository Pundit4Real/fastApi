from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet_val"
    resnet = "resnet_val"
    lenet = "lenet_val"

Books = {
    'book_1': {'title':'Title One','author':'Author ONe'},
    'book_2': {'title':'Title Two','author':'Author Two'},
    'book_3': {'title':'Title Three','author':'Author Three'},
    'book_4': {'title':'Title Four','author':'Author Four'},
    'book_5': {'title':'Title Five','author':'Author Five'},
    'book_6': {'title':'Title Six','author':'Author Six'}
}

@app.post('/')
async def create_new_book(book_title, book_author):
    current_id = 0
    if len(Books) > 0:
        for book in Books:
            book_id = int(book.split('_')[-1])
            if book_id > current_id:
                current_id = book_id

    new_book_id = f'book_{current_id + 1}'
    Books[new_book_id]= {'title':book_title, 'author':book_author}

    return Books[new_book_id]


@app.get('/')
async def Read_all_books(skip_book: Optional[str] = None
                         ):
    if skip_book:
        new_books = Books.copy()
        del new_books[skip_book]
        return new_books
    else:
        return Books



@app.get('/{book_name}')
async def read_book(book_name:str):
    return Books[book_name]


@app.put("/{book_id}")
async def update_book(book_id:str, book_title:str, book_author:str):
    book_information = {'title':book_title, 'author':book_author}
    Books[book_id]= book_information
    return book_information


@app.delete('/{book_id}')
async def delete_book(book_id):
    del Books[book_id]
    return f'Book{book_id} deleted.'

# @app.get('/users/usernames')
# async def usernames():
#     return {"user's name":"testing"}

# @app.get('/users/{userid}')
# async def read_userid(userid:int):
#     return {"user's name":userid}


# @app.get("/models/{model_name}")
# async def get_model(model_name:ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name":model_name, 'message':"Deep Learning FTW!!"}
#     elif model_name == ModelName.resnet:
#         return {"model_name": model_name, "message": "Have some residuals"}
#     else:
#         return {"model_name": model_name, "message": "LeCNN all the images"}