from database.database import get_connection

def save_chat(question, answer):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO chats (question, answer)
        VALUES (%s, %s)
        """,
        (question, answer)
    )

    connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    save_chat(
        "What is FastAPI?",
        "FastAPI is a Python web framework."
    )

    print("Chat saved successfully")