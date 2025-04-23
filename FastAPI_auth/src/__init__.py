from http.client import HTTPResponse
from fastapi import FastAPI , HTTPException , Response , status
from .routes.auth_route import router
from .routes.auth_route2 import router2
from .routes.auth_route3 import router3
# from pydantic import 

app = FastAPI()

version = "v1"
app = FastAPI(
    title="App",
    description="Testing Auth",
    version=version
)
app.include_router(router ,prefix="/api/{version}/auth" , tags=["auth"])
app.include_router(router2 ,prefix="/api/{version}/auth2" , tags=["auth2"])
app.include_router(router3 ,prefix="/api/{version}/auth3" , tags=["auth3"])

# uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)