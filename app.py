import sqlite3
import json
import database
from base64 import b64encode
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
    columns , results = get_select_all(table)
    
    con.close()
    return render_template (
        'index.html',
        table_name = table_name,
        columns = columns,
        results = results)

@app.route('/table/<tablename>')
def get_table(tablename):
    con = database.get_engine().connect()
    table = database.get_table(tablename)
    table = table.select().execute().fetchall()
    table_name = tablename
    
    columns , results = get_select_all(table)
        

    con.close()
    
    return render_template (
        'index.html',
        table_name = table_name,
        columns = columns,
        results = results
    )

def get_select_all(table):
    columns = table[0].keys()
    results = []
    
    for row in table:
        current_data = {}
        count = 0
        for value in row:
            if columns[count] == 'Photo':
                value = b64encode(value)
            current_data.update({columns[count]: value})
            count+=1
        results.append(current_data)
    return columns, results


if __name__ == '__main__':
    app.run(debug=True)
