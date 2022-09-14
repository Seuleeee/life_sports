from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship

from config.database import Base


class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(String, primary_key=True, index=True)
    password = Column(String)
    email = Column(String)
    nickname = Column(String, nullable=True)
