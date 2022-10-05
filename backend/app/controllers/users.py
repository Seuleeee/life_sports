from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.users import UsersCreateItem, UsersReadItem, UsersUpdateItem
from app.business.users import UserBusiness
from app.config.database import get_db

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/')
async def sign_up(user: UsersCreateItem = Depends(), db: Session = Depends(get_db)):
    return UserBusiness().create(db=db, user=user)


@router.get('/', response_model=list[UsersReadItem])
async def read_users(db: Session = Depends(get_db)):
    return UserBusiness().read_list(db=db)


@router.get('/{email}', response_model=UsersReadItem)
async def read_user(email: str, db: Session = Depends(get_db)):
    return UserBusiness().read(db=db, email=email)


@router.put('/{email}')
async def update_user(email: str, user: UsersUpdateItem, db: Session = Depends(get_db)):
    return UserBusiness().update(db=db, email=email, user=user)


@router.delete('/{email}')
async def delete_user(email: str, db: Session = Depends(get_db)):
    return UserBusiness().delete(db=db, email=email)
