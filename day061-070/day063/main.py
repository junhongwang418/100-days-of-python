from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.widgets import html5 as h5widgets
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bookshelf.db"
db = SQLAlchemy(app)


class Book(db.Model):
    global db
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


class AddForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = IntegerField(
        'Rating', widget=h5widgets.NumberInput(min=0, max=10, step=1), validators=[DataRequired()])
    submit = SubmitField('Add Book')


@ app.route('/')
def home():
    return render_template('index.html', books=Book.query.all())


@ app.route("/add", methods=('GET', 'POST'))
def add():
    form = AddForm()
    if form.validate_on_submit():
        global db
        book = Book(
            name=form.data['name'], author=form.data['author'], rating=form.data['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect('/')
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
