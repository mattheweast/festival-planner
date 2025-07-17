from fastapi import FastAPI
from backend.app.routers.post_router import post_router

app = FastAPI()

app.include_router(post_router)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}
