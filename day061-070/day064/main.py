from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

MOVIE_DATABASE_API_KEY = os.getenv('MOVIE_DATABASE_API_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    global db
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


# db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# db.session.add(new_movie)
# db.session.commit()


class MovieEditForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5",
                         validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class MovieAddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    movies = Movie.query.order_by(desc(Movie.rating)).limit(10).all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = MovieEditForm()
    if form.validate_on_submit():
        movie = Movie.query.get(request.args.get('id'))
        movie.rating = form.data['rating']
        movie.review = form.data['review']
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    global db
    movie = Movie.query.get(request.args.get('id'))
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = MovieAddForm()
    if form.validate_on_submit():
        params = {
            'api_key': MOVIE_DATABASE_API_KEY,
            'query': form.data['title']
        }
        response = requests.get(
            'https://api.themoviedb.org/3/search/movie', params=params)
        response.raise_for_status()
        movies = response.json()['results']
        return render_template('select.html', movies=movies)
    return render_template("add.html", form=form)


@app.route("/select")
def select():
    params = {
        'api_key': MOVIE_DATABASE_API_KEY
    }
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{request.args.get('id')}", params=params)
    response.raise_for_status()
    data = response.json()

    movie = Movie(title=data['title'], img_url=f"https://www.themoviedb.org/t/p/w1280/{data['poster_path']}",
                  year=data['release_date'][:4], description=data['overview'])
    db.session.add(movie)
    db.session.commit()

    return redirect(url_for('edit', id=movie.id))


if __name__ == '__main__':
    app.run(debug=True)
