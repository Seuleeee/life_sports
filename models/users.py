# TODO, Base 제거
from config.database import Base, meta
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String


users = Table('Users', meta,
              Column('user_id', String, primary_key=True, index=True),
              Column('password', String),
              Column('email', String),
              Column('nickname', String)
            )


class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(String, primary_key=True, index=True)
    password = Column(String)
    email = Column(String)
    nickname = Column(String, nullable=True)
