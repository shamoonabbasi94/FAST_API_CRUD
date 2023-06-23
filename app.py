from fastapi import FastAPI,Body, Depends

import schema

from models import Devteam
print('models has been imported')
from sqlalchemy.orm import sessionmaker
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
app=FastAPI()
#This will create our database if it doesent already exists
Base.metadata.create_all(engine)
Sessions = sessionmaker(bind=engine)
# sessions=Session()
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.post("/postmethod")
def addItem(item:schema.Devteam, session = Depends(get_session)):
    # name = Devteam(name = item.name)
    my_instance = Devteam(employee_id=item.employee_id,name=item.name, email=item.email)
    # email = Devteam(email = item.email)
    session.add(my_instance)
    # session.add(email)
    session.commit()
    # session.refresh(item)
    return item
@app.get("/getmethod")
def getItems(session: Session = Depends(get_session)):
    all_items = session.query(Devteam).all()
    first_item=session.query(Devteam).first()
    filter_query=session.query(Devteam).filter(Devteam.name=='huraira').all()
    filter_by_query=session.query(Devteam).filter_by(email='medi@testing.com').all()
    limit_order_by=session.query(Devteam).order_by(Devteam.employee_id.desc()).limit(2).all()
    like_arg=session.query(Devteam).filter(Devteam.email.like('%@gmail.com')).all()
    return like_arg

@app.put("/{id}")
def updateItem(id:int, item:schema.Devteam, session = Depends(get_session)):
    itemObject = session.query(Devteam).get(id)
    # import pdb;pdb.set_trace()
    itemObject.name = item.name
    # itemObject.employee_id = item.employee_id
    itemObject.email = item.email
    session.commit()   
    return itemObject