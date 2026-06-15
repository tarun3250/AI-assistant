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


def get_chat_history():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, question, answer, created_at
        FROM chats
        ORDER BY created_at ASC
    """)

    chats = cursor.fetchall()

    cursor.close()
    connection.close()

    return chats
# print(get_chat_history())
# print("all data printed")

def clear_chat_history():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM chats
        """
    )
    connection.commit()
    cursor.close()
    connection.close()

# if __name__ == "__main__":
#     clear_chat_history()
#     print("chat history cleared")