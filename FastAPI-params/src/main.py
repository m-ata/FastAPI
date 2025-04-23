from fastapi import FastAPI
from .params.route import router as param_router
from .file.route import router as file_router
app = FastAPI()

version = "v1"
app = FastAPI(
    title="App",
    description="Testing Auth",
    version=version
)
app.include_router(param_router ,prefix="/api/{version}/param" , tags=["param"])
app.include_router(file_router ,prefix="/api/{version}/files" , tags=["file"])
