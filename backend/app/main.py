from fastapi import FastAPI

from app.config.database import engine, Base
from app.controllers import users, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
