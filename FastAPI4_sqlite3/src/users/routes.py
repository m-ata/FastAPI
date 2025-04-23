from typing import List, Optional
from fastapi import  HTTPException , status , UploadFile
import fastapi
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

from .config import get_all_users_db ,get_user_db,update_user_db , add_users_db , delete_user_db# type: ignore
# book data 
from .user_data import users

# define single route 
user_router = fastapi.APIRouter()

# type of user | used in List not in dictionary
class User_Create(BaseModel):
    # id:int
    name:str
    age:str
    email:EmailStr

# Pydantic model
class User_Update(BaseModel):
    name: Optional[str]
    age: Optional[int]
    email: Optional[EmailStr]


@user_router.get("/{user_id}")
async def home(user_id:int):
    users = get_all_users_db()
    for user in users:
        # userId = int(user["id"])
        if user_id==user_id:
            result = get_user_db(user_id)
            return JSONResponse(content=dict(result))

# @user_router.get("/")
# async def get_users():
#     #explicit manaual control of Json response
#     users = get_all_users()
#     users_list = [dict(user) for user in users] # convert sqlite3.row into dict
#     return JSONResponse(content=users_list)


@user_router.get("/")
async def get_users():
    users = get_all_users_db()
    users_list = [dict(user) for user in users]  # Convert sqlite3.Row to dict to send in json
    return JSONResponse(content=users_list)

@user_router.patch("/{user_id}")
async def update_user_handler(user_id, update_User: User_Update):
    users = get_all_users_db()
    userId=int(user_id)
    for user in users:
        if user["id"] == userId:
            new_name = update_User.name or user["name"]
            new_age = update_User.age or user["age"]
            new_email = update_User.email or user["email"]

            result = update_user_db(user_id, new_name, new_age, new_email)

            if result:
                return JSONResponse(content={"status": "success", "message": "User updated"})
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {userId} not found"
    )

@user_router.post("/",status_code=status.HTTP_201_CREATED)
async def add_users(user : User_Create):
    # user_id = len(users)+1
    # users = get_all_users()

    # user = users.append({"id": user_id , "name":username, "age":userage, "email":useremail})

    result = await add_users_db(user.name, user.age, user.email)
    if result:
        print("---- RESULT ----",result)
    return {
        "status": "success",
        "message" : "User added successfully",
        # "user" : JSONResponse(user)
    }
    
@user_router.delete("/{user_id}",status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    # global users  
    users = get_all_users_db()
    
    for index, user in enumerate(users):
        if user["id"] == user_id:
            result = delete_user_db(user_id)
            if result:
                # deleted_user = users.pop(index)  
                return { 
                    "status": "success",
                    "message": "User deleted successfully",
                    "deleted_user": f"User deleted with ID {user_id}"
                }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {user_id} not found"
    )


@user_router.post("/upload")
async def upload_file(files:List[UploadFile]) :
    
    for file in files:
        print(file)
    return {
        "message" : "Files Uploaded Successfully",
        "status" : "success",
        "Files": [files]
    }


