from sqlalchemy.orm import Session

from app.models.users import Users
from app.schemas.users import UsersCreateItem, UsersUpdateItem

class UserService:
    def create(self, db: Session, user: UsersCreateItem):
        db_user = Users(
            email=user.email,
            password=user.password,
            nickname=user.nickname
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user.email

    def read_list(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Users).offset(skip).limit(limit).all()

    def read(self, db: Session, email: str):
        result = db.query(Users).filter(Users.email == email).first()
        return result

    def update(self, db: Session, email: str, user: UsersUpdateItem):
        db_user = db.query(Users).filter(Users.email == email).update({
                Users.nickname: user.nickname,
            }
        )
        db.commit()
        return db_user

    def delete(self, db: Session, email: str):
        db_user = db.query(Users).filter(Users.email == email).first()
        db.delete(db_user)
        db.commit()
        return db_user
