from fastapi import HTTPException
from sqlalchemy.orm import Session
import bcrypt

from app.schemas.users import UsersCreateItem, UsersUpdateItem
from app.services.user_service import UserService


class UserBusiness:
    def create(self, db: Session, user: UsersCreateItem):
        hashed_password: bytes = self.__hash_password(user.password)
        user.password = hashed_password
        return UserService().create(db, user)

    def __hash_password(self, plain_password: str):
        bytes_password: bytes = plain_password.encode('utf-8')
        salt: bytes = bcrypt.gensalt()
        hashed_password: bytes = bcrypt.hashpw(bytes_password, salt)
        return hashed_password

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

    def verify_password(self, input_password, stored_password) -> bool:
        return bcrypt.checkpw(input_password, stored_password)