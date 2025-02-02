from fastapi import FastAPI
from data_model import NewStudents,UpdateStudents

app = FastAPI(
    title= "My First FastAPI",
    description= "This is a very bascic app that can do CRUD operations",
    version= "0.1"
)

# Data
students = {
    1:{
        "name":"Alpha",
        "age": 20,
        "Roll": 101
    },
    2:{
        "name":"Alpha Go",
        "age": 200,
        "Roll": 102
    },
    3:{
        "name":"Alpha Go",
        "age": 200,
        "Roll": 102
    }
}

# CRUD Operations
"""
Endpoints are: CRUD
Create - POST
Read - GET
Update - PUT
Delete - DELETE
"""

@app.get("/")
def home():
    return {"Hello": "World"}


# get all the students
@app.get("/students")
def get_students():
    return students

# Get specific student
@app.get("/students/{std_id}")
def get_student(std_id:int):
    if std_id not in students:
        return {"Error":"Student not fount"}
    return students[std_id]

# add a student
@app.post("/add-student")
def add_student(std:NewStudents):
    if not students:
        new_id = 1
    else:
        new_id = max(students.keys()) + 1
        students[new_id] = std.model_dump()
        return {"Message":f"Student with id {new_id} has been added"}
    

# Update a student
@app.put("update-student/{std_id}")
def update_student(std_id:int, new_std:UpdateStudents):
    if std_id not in students:
        return {"Error": f"Record Not found for student with id {std_id}"}
    
    if new_std.name:
        students[std_id]['name'] = new_std.name
    if new_std.age:
        students[std_id]['age'] = new_std.age
    if new_std.Roll:
        students[std_id]['Roll'] = new_std.Roll

    return students


# Delete a student
@app.delete("/delete-student/{std_id}")
def delete_student(std_id:int):
    if std_id not in students:
        return {"Error": f"Record Not found for student with id {std_id}"}
    del students[std_id]
    return students