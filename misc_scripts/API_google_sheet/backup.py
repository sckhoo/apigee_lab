from turtle import title
from fastapi import FastAPI, Path, HTTPException
import pandas as pd
from typing import Optional
from pydantic import BaseModel
import gspread
import os
from typing import Optional

app = FastAPI(title="sckhoo FastAPI learning")

userdb = []

class UserClassIn(BaseModel):
    name: str
    age: int
    gender: Optional[str] = None
    icnum : str

class UserClass(BaseModel):
    name: str
    age: int
    gender: Optional[str] = None

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


@app.post("/postdata")
async def post_data(name_value: UserClass):
    print(name_value)
    return {
        "name": name_value.name
    }


@app.post("/user", response_model=UserClass)
async def put_user(username: UserClassIn, VIP: bool):
    userdb.append(username.dict())
    print(userdb)
    return {**username.dict()}