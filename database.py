# import pdb;pdb.set_trace()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#engine=create_engine


server = 'your_server_name'
database = 'your_DB_name'
username = 'username'
password = 'password'

# create the engine
engine = create_engine(f'mssql+pymssql://{username}:{password}@{server}/{database}')


Base=declarative_base()

SessionLocal=sessionmaker(bind=engine,expire_on_commit=False)