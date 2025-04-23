from ast import Dict
from collections import UserDict
import email
from email import message
from http.client import HTTPResponse
from fastapi import FastAPI, HTTPException , status , UploadFile
from fastapi.responses import JSONResponse  
from pydantic import BaseModel 
from typing import List, Dict , Union 
import uvicorn

app = FastAPI()

# type of user | used in List not in dictionary
# class User(BaseModel):
#     id:int
#     name:str
#     age:str
#     email:str

User_Dict = Dict[str, Union[str, int]]  # Values can be str or int

users:List[User_Dict]= [
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 28
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "age": 32
  },
  {
    "id": 3,
    "name": "Bob Johnson",
    "email": "bob@example.com",
    "age": 45
  },
  {
    "id": 4,
    "name": "Alice Williams",
    "email": "alice@example.com",
    "age": 24
  }
]

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/users/")
def get_users():
    #explicit manaual control of Json response
    return JSONResponse(users)

@app.put("/users/{user_id}")
async def update_user(user_id:int,user_name:str,user_email:str,user_age:str):
    for user in users:
        if user["id"]==user_id:
            user["name"]=user_name
            user["email"]=user_email
            user["age"]=user_age
            return JSONResponse(user)
        else:
            raise HTTPException(status_code=404, detail="User Not Found")


@app.post("/users/",status_code=status.HTTP_201_CREATED)
def add_users(username, userage, useremail):
    user_id = len(users)+1
    user = users.append({"id": user_id , "name":username, "age":userage, "email":useremail})
    return {
        "status": "success",
        "message" : "User added successfully",
        "user" : {"id": user_id , "name":username, "age":userage, "email":useremail}
    }
    
@app.delete("/users/{user_id}",status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    global users  
    
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)  
            return {
                "status": "success",
                "message": "User deleted successfully",
                "deleted_user": deleted_user 
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {user_id} not found"
    )


@app.post("/upload")
async def upload_file(files:List[UploadFile]) :
    
    for file in files:
        print(file)
    return {
        "message" : "Files Uploaded Successfully",
        "status" : "success",
        "Files": [files]
    }
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)