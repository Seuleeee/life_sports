from typing import List
from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from config.database import SessionLocal, engine, Base
from schemas.users import UsersCreateItem
from services.user_service import create_user


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/api/v1/users')
async def sign_up(user: UsersCreateItem, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    return db_user
