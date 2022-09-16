from fastapi import APIRouter
from type.user import Query, Mutation
from strawberry import Schema
from strawberry.asgi import GraphQL

from fastapi import FastAPI

user = APIRouter()
schema = Schema(Query, Mutation)
graphql_app = GraphQL(schema)


user.add_route('/graphql', graphql_app)


# ========== Restful API ===========
