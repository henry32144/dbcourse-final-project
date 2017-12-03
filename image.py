from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import mapper, scoped_session, sessionmaker
from sqlalchemy_imageattach.context import store_context

engine = create_engine('sqlite:///college.db', convert_unicode=True)
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo

class Academy(object):
    query = db_session.query_property()

    def __init__(self, AcademyNum=None, AcademyName=None,OfficeAddress=None, Dean=None, DServing=None ):
        self.AcademyNum = AcademyNum
        self.AcademyName = AcademyName
        self.OfficeAddress = OfficeAddress
        self.Dean = Dean
        self.DServing = DServing

    def __repr__(self):
        return '<Academy %r>' % (self.AcademyName)

academies = Table('Academy', metadata, autoload=True)

teachers = Table('Teacher', metadata, autoload=True)

courses = Table('Course', metadata, autoload=True)

students = Table('Student', metadata, autoload=True)

tcourse = Table('Take_Course', metadata, autoload=True)

con = engine.connect()

#------------------------------



