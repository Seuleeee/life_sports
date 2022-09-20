from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.users import UsersCreateItem, UsersReadItem, UsersUpdateItem
from business.users import UserBusiness
from config.database import get_db

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/')
async def sign_up(user: UsersCreateItem, db: Session = Depends(get_db)):
    return UserBusiness().create(db=db, user=user)


@router.get('/', response_model=list[UsersReadItem])
async def read_users(db: Session = Depends(get_db)):
    return UserBusiness().read_list(db=db)


@router.get('/{user_id}', response_model=UsersReadItem)
async def read_user(user_id: str, db: Session = Depends(get_db)):
    return UserBusiness().read(db=db, user_id=user_id)


@router.put('/{user_id}')
async def update_user(user_id: str, user: UsersUpdateItem, db: Session = Depends(get_db)):
    return UserBusiness().update(db=db, user_id=user_id, user=user)


@router.delete('/{user_id}')
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    return UserBusiness().delete(db=db, user_id=user_id)
