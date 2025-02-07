from fastapi import FastAPI
from routes.routes import router
from database.model import Translation
from database.database import Base, engine

app = FastAPI(
    title="Language Translation Service",
    description="This is a simple language translation service.",
    version="0.1"
)

# create the tables
Base.metadata.create_all(bind=engine)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)