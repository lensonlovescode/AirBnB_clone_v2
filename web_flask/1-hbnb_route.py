#!/usr/bin/python3
"""
Contains a script that starts a Flask web application 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """
    Displays “Hello HBNB!” on route /
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Displays HBNB on route /hbnb
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
