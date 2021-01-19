#!/usr/bin/python3
"""
script that starts a Flask web application:
- web application listen on 0.0.0.0, port 5000
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    "display Hello HBNB!"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def display_c(text):
    """Display C plus the string placed in the text variable."""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def display_python(text="is cool"):
    "Display by default Python is cool."
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """display n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_template(n):
    """display n is a number only if n is an integer inside
    5-number.html file"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_even_odd(n):
    """display n is a number only if n is an integer inside
    6-number_odd_or_even.html file"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
