from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from configbd.db import meta, engine

users = Table("Users", meta, 
Column("id", Integer, primary_key=True), 
Column("name", String(225)),
Column("email", String(225)),
Column("age", Integer()),
Column("password", String(225)),
mysql_charset = "utf8mb4"
)

meta.create_all(engine)