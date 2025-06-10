from fastapi import FastAPI

app = FastAPI()

# Route / Path Operation
@app.get("/")
def root():
    return{"message": "Welcome to my API"}
