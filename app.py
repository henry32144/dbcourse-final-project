import sqlite3
import json
import database
import base64
from demo_query import demo_query, demo_query_title
from flask import Flask, render_template, request, g , jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from datetime import datetime

#from sqlalchemy.orm import mapper, scoped_session, sessionmaker
# Initialize flask app.
app = Flask(__name__)

status_code = { 'operator_warn':"Only SELECT operator is accepted",
                'empty_warn':"Nothing input",
                'success':"Request has been send successful",
                'no_result':"Request has succeeded, but no result",
                'error':"An error occurred:",
}

@app.route('/')
def index():
    con = database.get_engine().connect()
    table = database.academies.select().execute().fetchall()
    table_name = 'Academy'
    columns , results = parse_result(table)
    
    con.close()
    return render_template (
        'index.html',
        table_name = table_name,
        columns = columns,
        results = results)

@app.route('/demo')
def demo():
    
    return render_template (
        'demo.html')

@app.route('/demo/<demoname>')
def get_demo(demoname):
    engine = database.get_engine()
    table_name = demoname
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


@app.route('/operation/submit', methods=['POST'])
def operation_submit():
    
    status = ''
    
    # Get text from requset.
    request_code = request.form.get('request-text')

    # Get text is not empty.
    if request_code != '':

        # Check if exist invalid operator.
        request_code = string_process(request_code)
        
        # Invalid operator exist, return warn.
        if request_code == 0:
            return render_template('operation.html',
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
                    return render_template('operation.html',
                        status = {'success':status_code['success']},
                        user_input = request_code,
                        columns = columns,
                        results = results)

                # Result is empty, show status message.
                else:
                    return render_template('operation.html',
                        status = {'success':status_code['no_result']},
                        user_input = request_code)

            # Something error occure, return error message.
            except Exception as ex:
                return render_template('operation.html',
                    status = {'error':status_code['error']},
                    user_input = request_code,
                    error_message = ex)

    return render_template (
        'operation.html',
        status = {'warn':status_code['empty_warn']})



##Database functions
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
    app.run(debug=True)
