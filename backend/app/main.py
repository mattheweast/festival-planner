from fastapi import FastAPI
from backend.app.routers.post_router import post_router
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

app.include_router(post_router)

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='matteast',
            password='admin',
            cursor_factory=RealDictCursor
            )
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print("Error: ", error)
        time.sleep(2)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}
