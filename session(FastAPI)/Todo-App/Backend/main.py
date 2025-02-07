from fastapi import FastAPI
from routes.routes import router
from routes.auth_routes import auth_route
# user name=sami606713   pass =$@m!u11@h

app = FastAPI(
    title= "Todo App",
    description= "This is a very bascic app that can do CRUD operations",
    version= "0.1"
)

app.include_router(router)
app.include_router(auth_route)


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)