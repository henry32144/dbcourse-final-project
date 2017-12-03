import sqlite3
import json
import database
from flask import Flask, render_template, request, g , jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from datetime import datetime

#from sqlalchemy.orm import mapper, scoped_session, sessionmaker
# Initialize flask app.
app = Flask(__name__)



@app.route('/')
def index():
    con = database.get_engine().connect()

    #academies_r = academies.select().execute().fetchall()
    return render_template (
        'index.html', 
    )


if __name__ == '__main__':
    app.run(debug=True)


@app.teardown_request
def shutdown_session(exception=None):
    con.close()
