#!/usr/bin/python3
"""
Contains a script that starts a Flask web application 0.0.0.0, port 5000
"""
from flask import Flask
from markupsafe import escape
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays “C ” followed by the value of the text variable
    """
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    Displays “Python ”, followed by the value of the text variable
    """
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return f"{escape(n)} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
