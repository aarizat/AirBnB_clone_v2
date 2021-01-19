#!/usr/bin/python3
"""
script that starts a Flask web application:
- web application listen on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def fetch_states():
    """Fetch states from DataBase"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exc):
    """Close session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)