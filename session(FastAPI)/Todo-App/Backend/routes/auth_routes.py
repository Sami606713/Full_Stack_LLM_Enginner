from fastapi import APIRouter,HTTPException
from models.model import UserRrgister,UserLogin
from db.database import user_collection
from routes.hash import hash_password,verify_password,create_access_token
from datetime import timedelta

auth_route = APIRouter()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# make a th routes for signup and login

@auth_route.post("/auth/register")
def register_user(user:UserRrgister):
    print(user.user_name)
    print(user.email)
    print(user.password)

    existing_user = user_collection.find_one({"email":user.email})
    # print(existing_user)
    if existing_user:
        return {"Error":"User Already Exist"}
    
    new_user = {
        "user_name":user.user_name,
        "email":user.email,
        "password":hash_password(user.password)
    }
    
    # inser the user
    user_collection.insert_one(dict(new_user))
    return {"Success": f"{user} Add scuueccfully"}


@auth_route.post("/auth/login")
def login_user(user:UserLogin):
    existing_user = user_collection.find_one({"email":user.email})

    # verify the user
    if not existing_user or not verify_password(user.password, existing_user['password']):
        return HTTPException(400,"UnAuthorized")
    
    # generate the access token
    access_token = create_access_token({"email":user.email},timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}


