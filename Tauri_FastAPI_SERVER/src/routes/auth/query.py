import sqlite3

from fastapi import HTTPException
from .model import DB_USER_MODEL, LOGIN_FormData , REGISTER_FormData, USER_MODEL , DB_ALL_USERS_MODEL

# controller 
from .controller import verify_password


def REGISTER_USER_DB(user:DB_USER_MODEL):
    connection = None

    try:
        connection = sqlite3.connect("desktop_app.db")
        cursor = connection.cursor()
        print(user)
        print("Inserting user data:")
        print(f"ID: {user.id}, Username: {user.username}, Fullname: {user.fullname}, Email: {user.email}")

        cursor.execute(
            """INSERT INTO users (id, username, fullname, email, hashpassword) VALUES (?, ?, ?, ?, ?)""",
            (user.id, user.username, user.fullname, user.email, user.hashpassword)
        )
        connection.commit()

    except sqlite3.IntegrityError as error:
        error_message = str(error)
        if "UNIQUE constraint failed" in error_message:
            user_message = "Error : Already Exist, Please use a different email or username."
        else:
            user_message = "Error occurred while adding new user."

        # print("DB Error:", error_message)

        raise HTTPException(
            detail=user_message,
            status_code=400,  
            headers={"X-DB-Error": error_message}
        ) 
    finally:
        if connection:
            connection.close() 


def LOGIN_USER_DB(user:LOGIN_FormData):
    connection = None
    print("RUNNING DB")

    try:
        connection = sqlite3.connect("desktop_app.db")
        cursor = connection.cursor()
        cursor.execute("SELECT id, username, hashpassword, email, fullname FROM users")
        rows = cursor.fetchall()

        if user.username:
            for row in rows:
                if user.username == row[1]:  # username match
                    hashed_password = row[2]
                    if verify_password(user.password, hashed_password):
                        fetched_user = USER_MODEL(
                            id=row[0],
                            username=row[1],
                            fullname=row[4],
                            email=row[3],
                        )
                        return fetched_user
                    else:
                        return False,
            return None

        elif user.email:
            for row in rows:
                if user.email == row[3]:  # email match
                    hashed_password = row[2]
                    if verify_password(user.password, hashed_password):
                        fetched_user = USER_MODEL(
                            id=row[0],
                            username=row[1],
                            fullname=row[4],
                            email=row[3],
                        )
                        return fetched_user
                    else:
                        return False 
            return None

        else:
            return None, "⚠️ Please provide username or email"

        # connection.commit()

    except sqlite3.IntegrityError as error:
        error_message = str(error)
        if "UNIQUE constraint failed" in error_message:
            user_message = "Error : Already Exist, Please use a different email or username."
        else:
            user_message = "Error occurred while adding new user."

        # print("DB Error:", error_message)

        raise HTTPException(
            detail=user_message,
            status_code=400,  
            headers={"X-DB-Error": error_message}
        ) 
    finally:
        if connection:
            connection.close() 



def GET_USERS_DB():
    connection = None

    try:
        connection = sqlite3.connect("desktop_app.db")
        cursor = connection.cursor()
        cursor.execute(
            """SELECT id, username, fullname, email FROM users"""
        )

        connection.commit()
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = USER_MODEL(
                id=row[0],
                username=row[1],
                fullname=row[2],
                email=row[3],
                # hashpassword=row[4],
            )
            users.append(user)
        # when all users fetch 
        return users
    except sqlite3.DataError:
        raise HTTPException(detail="SOMETHING WENT WRONG" , status_code=404)
    finally:
        if connection:
            connection.close()