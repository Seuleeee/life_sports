from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.users import UsersCreateItem, UsersUpdateItem
from services.user_service import UserService


class UserBusiness:
    def create(self, db: Session, user: UsersCreateItem):
        return UserService().create(db, user)

    def read_list(self, db: Session, skip: int = 0, limit: int = 100):
        return UserService().read_list(db, skip, limit)

    def read(self, db: Session, user_id: str):
        result = UserService().read(db, user_id)
        if not result:
            raise HTTPException(404, "Can't retrieve this user")
        return result

    def update(self, db: Session, user_id: str, user: UsersUpdateItem):
        return UserService().update(db, user_id, user)

    def delete(self, db: Session, user_id: str):
        return UserService().delete(db, user_id)