from fastapi import FastAPI
import uvicorn
from .users.routes import user_router

version = "v1"

app =  FastAPI(
    title="API Backend",
    description="Backend for Multiple API's",
    version=version
)

# here we can defines multiples routes 
app.include_router( user_router,prefix=f"/api/{version}/users" , tags=['users'])

# if __name__ == "__main__":
#     uvicorn.run("main:book_router", host="127.0.0.1", port=8000, reload=True)