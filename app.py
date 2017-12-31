import sqlite3
import json
import database
import base64
from demo_query import demo_query, demo_query_title
from flask import Flask, render_template, request, g , jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
import datetime, decimal

## Initialize flask app.
app = Flask(__name__)

status_code = { 'operator_warn':"Only SELECT operator is accepted",
                'empty_warn':"Nothing input",
                'success':"Request has been send successful",
                'no_result':"Request has succeeded, but no result",
                'error':"An error occurred:",
}

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

@app.route('/operation/update')
def update():
    
    return render_template (
        'update.html')

@app.route('/operation/delete')
def delete():
    
    return render_template (
        'delete.html')





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

@app.route('/table/<tablename>/query')
def query_request(tablename, methods=['GET']):
    con = database.get_engine().connect()
    query = request.args.get('text','')
    
    if query != '':
        columns, result = database.query_execute(tablename, query)
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
    app.run(debug=True)
