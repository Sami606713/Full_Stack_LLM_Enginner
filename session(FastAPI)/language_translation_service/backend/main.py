from fastapi import FastAPI
from routes.routes import router

app = FastAPI(
    title="Language Translation Service",
    description="This is a simple language translation service.",
    version="0.1"
)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)