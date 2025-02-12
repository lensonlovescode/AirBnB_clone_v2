#!/usr/bin/python3
"""
Contains a py script that starts a flask applications
"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception=None):
    """
    Closes the connection
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays the full hbnb page
    """
    diction = storage.all('State')
    sort_diction = dict(sorted(diction.items(), key=lambda item: item[1].name))
    return render_template('10-hbnb_filters.html', diction=sort_diction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
