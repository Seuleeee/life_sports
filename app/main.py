from fastapi import FastAPI

from config.database import engine, Base
from controllers import users

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)


# Dependency


