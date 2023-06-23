from sqlalchemy import Column, Integer, String
from database import Base


class Devteam(Base):
    _tablename_ = 'Devteam'
    employee_id = Column(Integer, primary_key=True)
    name=Column(String(256))
    email = Column(String(256))
class Users(Base):
    _tablename_='Users'
    id:Column(Integer,primary_key=True)
    name:Column(String(256))
    email:Column(String(256))   
    password:Column(String(256))