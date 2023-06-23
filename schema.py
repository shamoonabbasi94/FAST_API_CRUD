from pydantic import BaseModel

# class Item(BaseModel):
#     task:str

class Devteam(BaseModel):
    name:str
    employee_id:int
    email:str

class Users(BaseModel):
    id:int
    name:str
    email:str 
    password:str