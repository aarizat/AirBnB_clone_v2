#!/usr/bin/python3
"""
script that starts a Flask web application:
- web application listen on 0.0.0.0, port 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    "display Hello HBNB!"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    "Display HBNB"
    return "HBNB"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
