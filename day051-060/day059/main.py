import requests
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def root():
    response = requests.get('https://api.npoint.io/43644ec4f0013682fc0d')
    response.raise_for_status()
    data = response.json()
    return render_template("index.html", data=data)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:id>')
def post(id):
    response = requests.get('https://api.npoint.io/43644ec4f0013682fc0d')
    response.raise_for_status()
    data = list(filter(lambda post: post['id'] == id, response.json()))[0]
    return render_template("post.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
