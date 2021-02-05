import requests
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return render_template("home.html", username=username)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
