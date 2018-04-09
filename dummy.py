import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqLite import *
 
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","password","admin@mail.com")
session.add(user)
 
user = User("python","python","py@snailmail.com")
session.add(user)
 
user = User("jumpiness","python","swaru@outlook.com")
session.add(user)
 
# commit the record the database
session.commit()