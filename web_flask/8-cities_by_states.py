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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state_route():
    """
    Cities by States
    """
    diction = storage.all('State')
    sort_diction = dict(sorted(diction.items(), key=lambda item: item[1].name))
    return render_template('8-cities_by_states.html', diction=sort_diction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
