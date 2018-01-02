import sqlite3
import json
import database
import base64,sys
from demo_query import demo_query, demo_query_title
from flask import Flask, render_template, request, g , jsonify
from werkzeug import secure_filename
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
import datetime, decimal, time

## Initialize flask app.
app = Flask(__name__)

status_code = { 'operator_warn':"Only SELECT operator is accepted",
                'empty_warn':"Nothing input",
                'success':"Request has been send successful",
                'no_result':"Request has succeeded, but no result",
                'error':"An error occurred:",
}
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

## Get Academy table for default
@app.route('/')
def index():
    
    ##Get database engine
    con = database.get_engine().connect()

    ##Execute select all from Academy table
    table = database.academies.select().execute().fetchall()
    table_name = 'Academy'
    
    ##Parse result data
    columns , results = parse_result(table)
    
    con.close()
    return render_template (
        'index.html',
        table_name = table_name,
        columns = columns,
        results = results)

## Demo page
@app.route('/demo')
def demo():
    return render_template (
        'demo.html')

## Execute demo
@app.route('/demo/<demoname>')
def get_demo(demoname):
    engine = database.get_engine()
    table_name = demoname
    
    ## Get demo name by url
    
    demo_title = demo_query_title[demoname]
    demo_code = demo_query[demoname]

    demo_result = engine.execute(demo_code).fetchall()
    columns , results = parse_result(demo_result)

    
    return render_template (
        'demo.html',
        table_name = table_name,
        columns = columns,
        results = results,
        demo_title = demo_title,
        demo_code = demo_code
    )

##Operation page
@app.route('/operation')
def operation():
    
    return render_template (
        'operation.html')

@app.route('/operation/insert')
def insert():
    
    return render_template (
        'insert.html')

@app.route('/operation/insert/<tablename>', methods=['POST'])
def insert_new(tablename):
    table = database.get_table(tablename)
    columns = table.columns.keys()
    data = {}
    for i in columns:
        
        if i == 'DServing' or i == 'Bdate' or i == 'BDATE':
            temp = request.form.get(i,'')
            if temp == '':
                temp = time.strftime('%Y-%m-%d')
            temp = datetime.datetime.strptime(temp,'%Y-%m-%d')
        elif i == 'Photo':
            filename = request.files[i].filename
            temp = request.files[i].read()
            if filename == '':
                temp = read_default()
        else:
            temp = request.form.get(i,'')
        data[i] = temp
    print(data,file=sys.stderr)
    database.insert_data(tablename,data)

    columns, result = database.query_execute(tablename, data[table.primary_key.columns.keys()[0]])
    results = parse_query_result(columns, result)
    return render_template (
        'insert.html',
        columns = columns,
        results = results
        ) 


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def read_default():
    with open('./static/img/doge.png', 'rb') as f:
        photo = f.read()
    return photo

@app.route('/operation/update')
def update():
    ##Get database engine
    con = database.get_engine().connect()

    ##Execute select all from Academy table
    table = database.academies.select().execute().fetchall()
    table_name = 'Academy'
    
    ##Parse result data
    columns , results = parse_result(table)
    
    con.close()
    return render_template (
        'update.html',
        table_name = table_name,
        columns = columns,
        results = results)



@app.route('/operation/delete')
def delete():
        ##Get database engine
    con = database.get_engine().connect()

    ##Execute select all from Academy table
    table = database.academies.select().execute().fetchall()
    table_name = 'Academy'
    
    ##Parse result data
    columns , results = parse_result(table)
    
    con.close()
    return render_template (
        'delete.html',
        table_name = table_name,
        columns = columns,
        results = results)

@app.route('/operation/delete/table/<tablename>/delete', methods=['GET'])
def delete_item(tablename):
    con = database.get_engine().connect()
    data = request.values.get('key')
    print(data,file=sys.stderr)
    if data != '':
        if tablename == 'Take_Course':
            data = data.split('&')
            temp = []
            temp.append(data[0].split('=')[1])
            temp.append(data[1].split('=')[1])
            data = temp
        else:
            data = data.split('=')[1]
        database.delete_data(tablename, data)
    ##Execute select all from Academy table
    table = database.get_table(tablename)
    table = table.select().execute().fetchall()
    table_name = tablename
    
    ##Parse result data
    columns , results = parse_result(table)
    
    con.close()
    return render_template (
        'delete.html',
        table_name = table_name,
        columns = columns,
        results = results)


@app.route('/operation/<operation>/table/<tablename>')
def operation_get_table(operation, tablename):
    con = database.get_engine().connect()
    table = database.get_table(tablename)
    table = table.select().execute().fetchall()
    table_name = tablename
    
    columns , results = parse_result(table)       

    con.close()
    
    return render_template (
        operation + '.html',
        table_name = table_name,
        columns = columns,
        results = results
    )

@app.route('/operation/<operation>/table/<tablename>/query', methods=['GET'])
def operation_query_request(operation, tablename):
    con = database.get_engine().connect()
    query = request.args.get('text','')
    
    if query != '':
        columns, result = database.query_execute(tablename, query)
        data = parse_query_result(columns, result)
  
        json_data = json.dumps({'columns':columns, 'results':data})
        con.close()
        return json_data
    else:
        table = database.get_table(tablename)
        table = table.select().execute().fetchall()
        table_name = tablename  
        columns , data = parse_result(table)
        json_data = json.dumps({'columns':columns, 'results':data})
        return json_data


@app.route('/operation/get/academy-name')
def get_academy():
    result = database.engine.execute("SELECT AcademyName FROM Academy").fetchall()
    data = parse_name(result)
    json_data = json.dumps({'Name':data})
    return json_data

@app.route('/operation/get/teacher-name')
def get_teacher_name():
    result = database.engine.execute("SELECT Name FROM Teacher").fetchall()
    data = parse_name(result)
    json_data = json.dumps({'Name':data})
    return json_data

@app.route('/operation/get/teacher-num')
def get_teacher_number():
    result = database.engine.execute("SELECT Ssn FROM Teacher").fetchall()
    data = parse_name(result)
    json_data = json.dumps({'Number':data})
    return json_data

@app.route('/operation/get/student-num')
def get_student_number():
    result = database.engine.execute("SELECT StudentNum FROM Student").fetchall()
    data = parse_name(result)
    json_data = json.dumps({'Number':data})
    return json_data

@app.route('/operation/get/course-num')
def get_course_number():
    result = database.engine.execute("SELECT CourseNum FROM Course").fetchall()
    data = parse_name(result)
    json_data = json.dumps({'Number':data})
    return json_data

def parse_name(raw_result):
    data = []
    for i in raw_result:
        data.append(i[0])
    return data


##TextArea page
@app.route('/textarea')
def textarea():
    
    return render_template (
        'textarea.html')


@app.route('/textarea/submit', methods=['POST'])
def textarea_submit():
    
    status = ''
    
    # Get text from requset.
    request_code = request.form.get('request-text')

    # Get text is not empty.
    if request_code != '':

        # Check if exist invalid operator.
        request_code = string_process(request_code)
        
        # Invalid operator exist, return warn.
        if request_code == 0:
            return render_template('textarea.html',
                status = {'warn':status_code['operator_warn']},
                user_input = 'Nope')
        
        # Not exist, send code to database.
        else:
            try:
                engine = database.get_engine()
                cursor = engine.execute(request_code).fetchall()

                # Check if result is not empty.
                if cursor:
                        
                    #Parse result
                    columns , results = parse_result(cursor)
                    

                    # Success, return result.
                    return render_template('textarea.html',
                        status = {'success':status_code['success']},
                        user_input = request_code,
                        columns = columns,
                        results = results)

                # Result is empty, show status message.
                else:
                    return render_template('textarea.html',
                        status = {'success':status_code['no_result']},
                        user_input = request_code)

            # Something error occure, return error message.
            except Exception as ex:
                return render_template('textarea.html',
                    status = {'error':status_code['error']},
                    user_input = request_code,
                    error_message = ex)

    return render_template (
        'textarea.html',
        status = {'warn':status_code['empty_warn']})



## Get result by selected table
@app.route('/table/<tablename>')
def get_table(tablename):
    con = database.get_engine().connect()
    table = database.get_table(tablename)
    table = table.select().execute().fetchall()
    table_name = tablename
    
    columns , results = parse_result(table)       

    con.close()
    
    return render_template (
        'index.html',
        table_name = table_name,
        columns = columns,
        results = results
    )

@app.route('/table/<tablename>/query', methods=['GET'])
def query_request(tablename):
    con = database.get_engine().connect()
    query = request.args.get('text','')
    
    if query != '':
        columns, result = database.query_execute(tablename, query)
        data = parse_query_result(columns, result)
  
        json_data = json.dumps({'columns':columns, 'results':data})
        con.close()
        return json_data
    else:
        table = database.get_table(tablename)
        table = table.select().execute().fetchall()
        table_name = tablename  
        columns , data = parse_result(table)
        json_data = json.dumps({'columns':columns, 'results':data})
        return json_data

def parse_query_result(columns, result):
    data = []
    for row in result:
        current_data = {}
        count = 0
        for value in row:
            if columns[count] == 'Photo':
                ##To decode b'' header and encode img to base64
                value = base64.b64encode(value).decode('UTF-8')
            elif isinstance(value, datetime.date):
                value = value.strftime('%Y-%m-%d')
            elif isinstance(value, decimal.Decimal):
                value = str(value)
            current_data.update({columns[count]: value})
            count+=1
        data.append(current_data)
    return data

def parse_result(table):
    columns = table[0].keys()
    results = []
    
    for row in table:
        current_data = {}
        count = 0
        for value in row:
            if columns[count] == 'Photo':
                ##To decode b'' header and encode img to base64
                value = base64.b64encode(value).decode('UTF-8')
            elif isinstance(value, datetime.date):
                value = value.strftime('%Y-%m-%d')
            elif isinstance(value, decimal.Decimal):
                value = str(value)
            current_data.update({columns[count]: value})
            count+=1
        results.append(current_data)
    return columns, results

# This function check invalid text and filter the text.
def string_process(query_str):
    is_valid = True
    query_str = query_str.replace('\'','\"')
    unavaliabe = ['DELETE','DROP','UPDATE','CREATE']
    for i in unavaliabe:
        if query_str.find(i) != -1:
            is_valid = False
    if is_valid != True:
        return 0
    else:
        return query_str


if __name__ == '__main__':
    app.run(debug=False)
