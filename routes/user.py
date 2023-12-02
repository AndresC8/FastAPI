from fastapi import APIRouter
from configbd.db import conn
from models.user import users

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/c8")
def function1():
    return "Todo ok"

@user.get("/us")
def function2():
    return "pass"

@user.get("/use")
def function3():
    return "pass"

@user.get("/usrs")
def function4():
    return "pass"
