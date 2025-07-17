import psycopg2
from psycopg2.extras import RealDictCursor
import time

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
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print("Error: ", error)
        time.sleep(2)
