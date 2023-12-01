from sqlalchemy import create_engine, MetaData
from configbd import conn
from models import users


cengine = create_engine("mysql+pymysql://root:admin@localhost:3306/users_db")
meta = MetaData()
conn = cengine.connect()
