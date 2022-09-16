from models.users import Users
from config.database import engine, meta
from models.users import users

meta.create_all(engine)