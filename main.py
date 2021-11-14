#Python
from typing import Optional
from fastapi.param_functions import Query

#Pydantic
from pydantic import BaseModel

#FastApi
from fastapi import FastAPI
from fastapi import Body, Query


app = FastAPI()
#models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get('/')
async def home():
    return {'message': '<h1>Hello World</h1>'}


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

@app.get("/person/details")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length = 50),
    age: str = Query(...)
):
    return {name:age}