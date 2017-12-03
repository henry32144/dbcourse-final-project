from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

# Sqlite database path.
SQLITE_DB_PATH = 'college.db'

engine = create_engine('sqlite:///college.db', convert_unicode=True)
metadata = MetaData(bind=engine)

academies = Table('Academy', metadata, autoload=True)
teachers = Table('Teacher', metadata, autoload=True)
courses = Table('Course', metadata, autoload=True)
students = Table('Student', metadata, autoload=True)
tcourse = Table('Take_Course', metadata, autoload=True)

def get_engine():
    return engine


