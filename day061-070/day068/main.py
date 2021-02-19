from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()

        if user:
            return render_template('register.html', error='Email already exists')

        password = generate_password_hash(request.form.get('password'))
        user = User(email=email, name=request.form.get(
            'name'), password=password)
        db.session.add(user)
        db.session.commit()

        login_user(user)

        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()

        if not user:
            return render_template('login.html', error='Password incorrect. Please try again.')
        elif check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            return render_template('login.html', error='Password incorrect. Please try again.')

    return render_template('login.html')


@app.route('/secrets')
def secrets():
    if current_user.is_authenticated:
        return render_template("secrets.html", user=current_user)
    return abort(404)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    if current_user.is_authenticated:
        return send_from_directory('static/files', 'cheat_sheet.pdf')
    return abort(404)


if __name__ == "__main__":
    app.run(debug=True)
