from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.users import UsersCreateItem, UsersUpdateItem
from app.services.user_service import UserService
from app.utils.auth_utils import hash_password


class UserBusiness:
    def create(self, db: Session, user: UsersCreateItem):
        hashed_password: bytes = hash_password(user.password)
        user.password = hashed_password
        return UserService().create(db, user)

    def read_list(self, db: Session, skip: int = 0, limit: int = 100):
        return UserService().read_list(db, skip, limit)

    def read(self, db: Session, email: str):
        result = UserService().read(db, email)
        if not result:
            raise HTTPException(404, "Can't retrieve this user")
        return result

    def update(self, db: Session, email: str, user: UsersUpdateItem):
        return UserService().update(db, email, user)

    def delete(self, db: Session, email: str):
        return UserService().delete(db, email)
