from fastapi import FastAPI
import uvicorn
from .users.routes import user_router
from .users.config import create_table
version = "v1"

# CREATE_TABLE()
app =  FastAPI(
    title="API Backend",
    description="Backend for Multiple API's",
    version=version
)
create_table()
# here we can defines multiples routes 
app.include_router( user_router,prefix=f"/api/{version}/users" , tags=['users'])

# if __name__ == "__main__":
#     uvicorn.run("main:book_router", host="127.0.0.1", port=8000, reload=True)