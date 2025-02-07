#!/usr/bin/python3
"""
Contains a script that starts a Flask web application 0.0.0.0, port 5000
"""
from flask import Flask
from markupsafe import escape
from flask import render_template
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
    """
    Displays a HTML page only if n is an integer
    """
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays a HTML page only if n is an integer
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    Displays a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if (n % 2) == 0:
        return render_template('6-number_odd_or_even.html',
                               number=n, iswhat="is even")
    else:
        return render_template('6-number_odd_or_even.html',
                               number=n, iswhat="is odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
