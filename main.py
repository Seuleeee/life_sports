from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.database import SessionLocal, engine, Base
from schemas.users import UsersCreateItem, UsersReadItem, UsersUpdateItem
from services.user_service import UserService

from controllers.index import user

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(user)

# ============== Restful API ===============


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users', tags=['users'])
async def sign_up(user: UsersCreateItem, db: Session = Depends(get_db)):
    db_user = UserService().create(db=db, user=user)
    return db_user


@app.get('/users', tags=['users'], response_model=List[UsersReadItem])
async def read_users(db: Session = Depends(get_db)):
    db_user = UserService().read_list(db=db)
    return db_user


@app.get('/users/{user_id}', tags=['users'], response_model=UsersReadItem)
async def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = UserService().read(db=db, user_id=user_id)
    return db_user


@app.put('/users/{user_id}', tags=['users'])
async def update_user(user_id: str, user: UsersUpdateItem, db: Session = Depends(get_db)):
    db_user = UserService().update(db=db, user_id=user_id, user=user)
    return db_user


@app.delete('/users/{user_id}', tags=['users'])
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    db_user = UserService().delete(db=db, user_id=user_id)
    return db_user
