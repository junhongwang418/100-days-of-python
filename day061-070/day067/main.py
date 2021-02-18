from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


# Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CONFIGURE TABLE


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = CreatePostForm()

    if form.validate_on_submit():
        post = BlogPost(title=form.data['title'], subtitle=form.data['subtitle'], date=date.today().strftime(
            '%B %d, %Y'), body=form.data['body'], author=form.data['author'], img_url=form.data['img_url'])
        db.session.add(post)
        db.session.commit()
        return redirect("/")

    return render_template("make-post.html", form=form)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = BlogPost.query.all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    form = CreatePostForm(title=post.title, subtitle=post.subtitle,
                          author=post.author, img_url=post.img_url, body=post.body)

    if form.validate_on_submit():
        post.title = form.data['title']
        post.subtitle = form.data['subtitle']
        post.date = date.today().strftime('%B %d, %Y')
        post.body = form.data['body']
        post.author = form.data['author']
        post.img_url = form.data['img_url']
        db.session.commit()
        return redirect("/")

    return render_template("make-post.html", form=form)


@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
