from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title='users API',
    description='restAPI with python'
    version='0.0.1',
)

app.include_router(user)

