from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
from sqlalchemy_imageattach.context import store_context

##db path need to be changed
engine = create_engine('sqlite:///college.db', convert_unicode=True)
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo


academies = Table('Academy', metadata, autoload=True)

teachers = Table('Teacher', metadata, autoload=True)

courses = Table('Course', metadata, autoload=True)

students = Table('Student', metadata, autoload=True)

tcourse = Table('Take_Course', metadata, autoload=True)

con = engine.connect()

#------------------------------



