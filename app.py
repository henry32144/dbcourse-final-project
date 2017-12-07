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

@app.route('/operation')
def operation():
    
    return render_template (
        'operation.html')


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


if __name__ == '__main__':
    app.run(debug=True)
