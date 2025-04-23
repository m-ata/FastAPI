import sqlite3

connection = sqlite3.connect('users_db')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

def create_table():
    print("----TABLE CREATED IF NOT EXISTS----")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL,
            age TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
    )
    connection.commit()

async def add_users_db(name , age , email):
    cursor.execute(
        """
        INSERT INTO users (name , age , email) VALUES (? , ? , ? )
        """,
        (name, age , email,)
    )
    connection.commit()
    return True

def update_user_db(userId, newName, newAge , newEmail):
    cursor.execute(
        """
        UPDATE users SET name = ?, age = ?, email = ? WHERE id = ?
        """,
        (newName, newAge , newEmail,userId,)
    )
    connection.commit()
    return True

def delete_user_db(user_id):
    cursor.execute(
        """
        DELETE FROM users WHERE id = ?
        """,
        (user_id,)
    )
    connection.commit()
    return True
  
# def get_all_users():
#     cursor.execute(
#         """
#         SELECT * FROM users
#         """
#     )

#     users = cursor.fetchall()
#     return users


def get_all_users_db():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


def get_user_db(user_id):
    cursor.execute(
        """
        SELECT id, name, email, age 
        FROM users 
        WHERE id = ?
        """,
        (user_id,)  # ⬅️ tuple!
    )
    user = cursor.fetchone()
    return user