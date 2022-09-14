import datetime
from sqlalchemy.orm import Session

from models.users import Users
from schemas.users import UsersCreateItem


def create_user(db: Session, user: UsersCreateItem):
    db_user = Users(
        user_id=user.user_id,
        email=user.email,
        password=user.password,
        nickname=user.nickname
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
