from sqlalchemy import Column, String

from app.config.database import Base


class Users(Base):
    __tablename__ = 'Users'

    password = Column(String, primary_key=True, index=True)
    email = Column(String)
    nickname = Column(String, nullable=True)
