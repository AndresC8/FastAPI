from fastapi import APIRouter
from configbd.db import conn
from models.user import users

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/d")
def passs():
    return "pass"

@user.get("/usfers")
def passs():
    return "pass"

@user.get("/a")
def passs():
    return "pass"

@user.get("/ee")
def passs():
    return "pass"
