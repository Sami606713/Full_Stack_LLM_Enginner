from fastapi import APIRouter,Depends
from models.model import MyTodo,UpdateTodo
from bson import ObjectId
from schema.schema import list_serlarizer
from db.database import collection
from routes.hash import get_current_user
import logging
logging.info("Import successfully")

router = APIRouter()


@router.get("/")
def index():
    return {"home":"Welcome to the Todo App"}


# Get all todos
@router.get("/todos")
def get_todo(dict = Depends(get_current_user)):
    return list_serlarizer(collection.find())


# get to by id
@router.get("/todos/{id}")
def get_by_id(id:str, dict = Depends(get_current_user)):
    todo = collection.find_one({"_id":ObjectId(id)})
    print(todo)
    return {
        "id": str(todo['_id']),
        "title":todo['title'],
        "description":todo['description'],
        "complete":todo['complete']
    }


@router.post("/todos")
def create_todo(data:MyTodo, dict = Depends(get_current_user)):
    collection.insert_one(dict(data))
    return dict(data)


@router.put("/todos/{id}")
def update_todo(id:str,new_todo:UpdateTodo, dict = Depends(get_current_user)):
    collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(new_todo)})

    return {"Success":f"todo with {id} update successfully"}


# Delete a todo
@router.delete("/todos/{id}")
def delete_toto(id:str,dict = Depends(get_current_user)):
    collection.find_one_and_delete({"_id":ObjectId(id)})
    return {"Success":f"Todo {id} delete successfully"}
