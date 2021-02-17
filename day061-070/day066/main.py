from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import json

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafes = Cafe.query.all()
    cafe = random.choice(cafes)
    return jsonify(cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = Cafe.query.all()
    return jsonify([cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    location = request.args.get('location')
    cafes = Cafe.query.filter_by(location=location).all()
    return jsonify([cafe.to_dict() for cafe in cafes])


# HTTP POST - Create Record
@app.route("/new", methods=['POST'])
def new_cafe():
    name = request.data.get('name')
    map_url = request.data.get('map_url')
    img_url = request.data.get('map_url')
    seats = request.data.get('seats')
    has_toilet = bool(request.data.get('has_toilet'))
    has_wifi = bool(request.data.get('has_wifi'))
    has_sockets = bool(request.data.get('has_sockets'))
    can_take_calls = bool(request.data.get('can_take_calls'))
    coffee_price = request.data.get('coffee_price')
    cafe = Cafe(name=name, map_url=map_url, img_url=img_url, seats=seats, has_toilet=has_toilet,
                has_wifi=has_wifi, has_sockets=has_sockets, can_take_calls=can_take_calls, coffee_price=coffee_price)
    db.session.add(cafe)
    db.session.commit()
    return jsonify(cafe.to_dict())


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    cafe.price = request.data.get('price')
    db.session.commit()
    return jsonify(cafe.to_dict())


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def report_closed(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(cafe.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
