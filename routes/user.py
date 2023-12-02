from fastapi import APIRouter
from configbd.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    sql = conn.execute(users.insert().values(new_user))

    return conn.execute(users.select().where(users.c.id == sql.lastrowid)).first()

@user.get("/us")
def function2():
    return "pass"

@user.get("/use")
def function3():
    return "pass"

@user.get("/usrs")
def function4():
    return "pass"
