from fastapi import FastAPI

# FastAPI Instance
app = FastAPI()

# Route / Path Operation
@app.get("/")
def root():
    return{"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return{"data": "You're Posts"}

@app.post("/createposts")
def create_post():
    return {"message": "Successfully created post"}