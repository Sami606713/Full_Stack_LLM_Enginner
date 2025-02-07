from pydantic import BaseModel
from typing import Optional

class MyTodo(BaseModel):
    title:str
    description:str
    complete:bool = False 

class UpdateTodo(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    complete:Optional[bool] = None


class UserRrgister(BaseModel):
    user_name:str
    email:str
    password:str

class UserLogin(BaseModel):
    email:str
    password:str