from fastapi import FastAPI

from config.database import SessionLocal, engine, Base
from controllers.index import users


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)


# Dependency


