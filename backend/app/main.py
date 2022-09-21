from fastapi import FastAPI

from app.config.database import engine, Base
from app.controllers import users

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
