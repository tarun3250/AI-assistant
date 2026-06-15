import psycopg

DB_NAME = "ai_assistant"
DB_USER = "tarun"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    connection = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        host=DB_HOST,
        port=DB_PORT
    )
    return connection

if __name__ == "__main__":
    connection = get_connection()

    if connection:
        print("Database connected successfully")

    connection.close()