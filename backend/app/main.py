from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

# FastAPI Instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# Route / Path Operation
@app.get("/")
def root():
    return{"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return{"data": "You're Posts"}

@app.post("/createposts")
def create_post(post: Post):
    print (post.model_dump())
    return {"data": "new post"}
