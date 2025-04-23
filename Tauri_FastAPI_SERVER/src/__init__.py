from fastapi import FastAPI
from .routes.auth.route import router as auth_router
from fastapi.middleware.cors import CORSMiddleware 
from .db.database import init_db
app = FastAPI()

version = "v1"
origins=["http://localhost:1420","tauri://localhost","null"]

app = FastAPI(
    title="App",
    description="Testing Auth",
    version=version
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# connect sqlite3 db 
@app.on_event("startup")
async def ConnectDB():
    await init_db()

# other routes  
app.include_router(auth_router ,prefix="/api/{version}/auth" , tags=["auth"])