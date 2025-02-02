# Fastapi
- In this session we will learn everything about `fastapi`.

# Create a simple app
```bash
from fastapi import FastAPI

app = FastAPI(
    "title": "My First FastAPI",
    "description": "This is a very bascic app that can do CRUD operations",
    "version": "0.1.0",

)


@app.get("/")
def home():
    return {"Hello": "World"}
```

# How to run the app
```bash
fastapi dev name_of_file.py
```