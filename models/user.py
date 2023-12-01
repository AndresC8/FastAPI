from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer
from configbd.db import meta, cengine

users = Table("Users", meta, 
Column("id", Integer, primary_key=True), 
Column("name", string(225)),
Column("email", String(225)),
Column("age", Integer(2)),
Column("password", string(225)))

meta.create_all(cengine)