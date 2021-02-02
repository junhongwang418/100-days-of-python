from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
    response.raise_for_status()
    data = response.json()
    return render_template("index.html", data=data)


@app.route('/post/<int:id>')
def post(id):
    response = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
    response.raise_for_status()
    data = list(filter(lambda post: post['id'] == id, response.json()))[0]
    return render_template("post.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
