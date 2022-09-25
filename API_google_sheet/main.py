from fastapi import FastAPI, Path
import pandas as pd
from typing import Optional
from pydantic import BaseModel
import gspread
import os

app = FastAPI()

user_list = []

class UserClass(BaseModel):
    name: str
    age: int
    gender: str

@app.get("/")
async def hello():
    return {
        "message": "Hello World"
    }

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

@app.post("/postdata")
async def post_data(name_value: UserClass):
    print(name_value)
    return {
        "name": name_value.name
    }