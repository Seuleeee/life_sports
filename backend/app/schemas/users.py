from dataclasses import dataclass
from pydantic import BaseModel, Field, EmailStr
from fastapi import Form


@dataclass
class UsersCreateItem:
    email: EmailStr = Form(description='이메일')
    password: str = Form(min_length=8, max_length=20)
    nickname: str = Form(min_length=2, max_length=10)

    class Config:
        orm_mode = True


class UsersUpdateItem(BaseModel):
    nickname: str | None = Field(
        min_length=2, max_length=8, description='닉네임은 2~8글자의 영문 또는 한글로 만들어주세요.'
    )

    class Config:
        orm_mode = True


class UsersReadItem(BaseModel):
    email: EmailStr
    nickname: str

    class Config:
        orm_mode = True
