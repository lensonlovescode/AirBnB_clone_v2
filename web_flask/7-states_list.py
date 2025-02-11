#!/usr/bin/python3
"""
Contains a py script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
import sys
import os
from models import storage
sys.path.append(os.path.abspath(".."))


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
    for key, value in storage.all().items():
        arr = key.split('.')
        name = value.name
        id = arr[1]
        diction[id] = name
    return render_template('7-states_list.html', diction=diction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
