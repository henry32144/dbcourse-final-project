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
all_table = {'Academy':academies,'Teacher':teachers,
            'Course':courses,'Student':students,'Take_Course':tcourse}

def get_engine():
    return engine


def get_table(tablename):
    return all_table[tablename]

def query_execute(tablename, parameter):
    table = get_table(tablename)
    columns = table.columns.keys()
    result = ''
    if tablename == "Academy":
        result = table.select().where(table.c.AcademyNum.like("%{}%".format(parameter))).execute().fetchall()
    elif tablename == "Teacher":
        result = table.select().where(table.c.Ssn.like("%{}%".format(parameter))).execute().fetchall()
    elif tablename == "Course":
        result = table.select().where(table.c.CourseNum.like("%{}%".format(parameter))).execute().fetchall()
    elif tablename == "Student":
        result = table.select().where(table.c.StudentNum.like("%{}%".format(parameter))).execute().fetchall()
    elif tablename == "Take_Course":
        result = table.select().where(table.c.SNum.like("%{}%".format(parameter))).execute().fetchall()
    return columns, result

def insert_data(tablename, data):
    table = get_table(tablename)
    engine.connect().execute(table.insert().values(data))

def delete_data(tablename, data):
    table = get_table(tablename)
    engine.connect().execute(table.delete().where(data))

