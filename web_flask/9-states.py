#!/usr/bin/python3
"""
Contains a py script that starts a flask application
"""
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception=None):
    """
    Closes the db session
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def application_route():
    """
    Displays all models
    """
    diction = storage.all('State')
    sort_diction = dict(sorted(diction.items(), key=lambda item: item[1].name))
    return render_template('7-states_list.html', diction=sort_diction)


@app.route('/states/<id>')
def specific_state(id):
    """
    Specific states is displayed
    """
    for k, v in storage.all('State').items():
        if v.id == id:
            return render_template('9-states.html',
                                   state_name=v.name, cities=v.cities)

    return render_template('404.html')


@app.errorhandler(404)
def page_not_found(e):
    """
    A custom 404 page
    """
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
