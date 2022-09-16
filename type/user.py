import strawberry
from config.database import conn
from models.index import users


@strawberry.type
class Users:
    user_id: str
    password: str
    email: str
    nickname: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self, info, user_id: str) -> Users:
        return conn.execute(users.select().where(users.c.user_id == user_id)).fetchone()

    @strawberry.field
    def users(self, info) -> list[Users]:
        return conn.execute(users.select()).fetchall()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, user_id: str, password: str, email: str, nickname: str) -> str:
        result = conn.execute(users.insert().values(user_id=user_id, password=password, email=email, nickname=nickname))
        return str(result.inserted_primary_key[0])

    @strawberry.mutation
    def update_user(self, info, user_id: str, email: str, nickname: str) -> int:
        result = conn.execute(users.update().where(users.c.user_id == user_id).values(email=email, nickname=nickname))
        # return conn.execute(users.select().where(users.c.user_id == user_id)).fetchone()
        return result.rowcount

    @strawberry.mutation
    def delete_user(self, info, user_id: str) -> bool:
        result = conn.execute(users.delete().where(users.c.user_id == user_id))
        return result.rowcount > 0



