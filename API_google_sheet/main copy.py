from fastapi import FastAPI, Path
import pandas as pd
from typing import Optional
from pydantic import BaseModel
import gspread
import os

print(os.getcwd())
sa = gspread.service_account("sa.json")
sh = sa.open("phone number")

wks = sh.worksheet("Phone")

#print("Rows", wks.row_count)
#print("Cols", wks.col_count)
#print(wks.acell('B2').value)
#print(wks.get('A2:B2'))
#wks.update('A3', "Megan")
#wks.update('A5:B5', [["Ashlee",'987654']])
#wks.update('C2', '=UPPER(A2)', raw=False)

# with github

app = FastAPI()

class Books(BaseModel):
    title: str
    author: str
    date: str

books = {
    1: {
        "title": "test1 title",
        "author": "test1 author",
        "date": "test1 date"
    },
    3: {
        "title": "test3 title",
        "author": "test3 author",
        "date": "test3 date"
    }
}

user_list = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/name")
async def root():
    return {"name": "sckhoo"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/add/{x}/{y}")
async def addition(x:int, y:int):
    return {"total": x+y}

@app.get("/get_book/{title_id}")
async def get_book(title_id: int = Path(None, description="Need the title ID of the book", gt=0, le=len(books))):
    return books[title_id]
    #return len(books)

@app.get("/get_by_title")
async def get_title(*, title : Optional[str] = None, test: int):
    #return books[title_id]
    for book in books:
        if books[book]['title'] == title:
            return books[book]
    return {"data" : "book not found"}

@app.get("/user/{username}")
async def put_user(username: str):
    return user_list

@app.put("/user/{username}")
async def put_user(username: str):
    user_list.append(username)
    return user_list

@app.post("/user")
async def put_user(username: str):
    user_list.append(username)
    return user_list