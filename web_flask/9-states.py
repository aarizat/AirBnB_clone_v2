#!/usr/bin/python3
"""
script that starts a Flask web application:
- web application listen on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<string:id>", strict_slashes=False)
def fetch_state_and_cities(id=None):
    """Fetch states from DataBase"""
    states = storage.all(State)
    if id is None:
        return render_template("9-states.html", states=states)
    return render_template("9-states.html", states=states, id="State." + id)


@app.teardown_appcontext
def close_session(exc):
    """Close session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
