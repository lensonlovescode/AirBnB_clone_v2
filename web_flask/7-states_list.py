#!/usr/bin/python3
"""
Contains a py script that starts a Flask web application
"""
import os
import sys
sys.path.append(os.path.abspath(".."))
from models import storage
from flask import Flask
from flask import render_template



app = Flask(__name__)


@app.teardown_appcontext
def close_db_session(exception=None):
    """
    Closes the database session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def application_route():
    """
    Displays all models
    """
    diction = {}
    for key, value in storage.all('State').items():
        arr = key.split('.')
        name = value.name
        id = arr[1]
        diction[id] = name
    sorted_diction = dict(sorted(diction.items(), key=lambda item: item[1]))
    return render_template('7-states_list.html', diction=sorted_diction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
