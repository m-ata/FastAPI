from typing import List
from fastapi import  HTTPException , status , UploadFile
import fastapi
from fastapi.responses import JSONResponse  

# book data 
from .user_data import users

# define single route 
user_router = fastapi.APIRouter()

# type of user | used in List not in dictionary
# class User(BaseModel):
#     id:int
#     name:str
#     age:str
#     email:str

@user_router.get("/hello")
async def home():
    return {"message": "Hello FastAPI"}

@user_router.get("/")
async def get_users():
    #explicit manaual control of Json response
    return JSONResponse(users)

@user_router.patch("/{user_id}")
async def update_user(user_id:int,user_name:str,user_email:str,user_age:str):
    for user in users:
        if user["id"]==user_id:
            user["name"]=user_name
            user["email"]=user_email
            user["age"]=user_age
            return JSONResponse(user)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {user_id} not found"
    )

@user_router.post("/",status_code=status.HTTP_201_CREATED)
async def add_users(username, userage, useremail):
    user_id = len(users)+1
    user = users.append({"id": user_id , "name":username, "age":userage, "email":useremail})
    return {
        "status": "success",
        "message" : "User added successfully",
        "user" : JSONResponse(user)
    }
    
@user_router.delete("/{user_id}",status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    global users  
    
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)  
            return {
                "status": "success",
                "message": "User deleted successfully",
                "deleted_user": JSONResponse(deleted_user) 
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


