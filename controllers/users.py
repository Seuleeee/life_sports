from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.users import UsersCreateItem, UsersReadItem, UsersUpdateItem
from services.user_service import UserService
from config.database import get_db

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/')
async def sign_up(user: UsersCreateItem, db: Session = Depends(get_db)):
    db_user = UserService().create(db=db, user=user)
    return db_user


@router.get('/', response_model=list[UsersReadItem])
async def read_users(db: Session = Depends(get_db)):
    db_user = UserService().read_list(db=db)
    return db_user


@router.get('/{user_id}', response_model=UsersReadItem)
async def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = UserService().read(db=db, user_id=user_id)
    return db_user


@router.put('/{user_id}')
async def update_user(user_id: str, user: UsersUpdateItem, db: Session = Depends(get_db)):
    db_user = UserService().update(db=db, user_id=user_id, user=user)
    return db_user


@router.delete('/{user_id}')
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    db_user = UserService().delete(db=db, user_id=user_id)
    return db_user
