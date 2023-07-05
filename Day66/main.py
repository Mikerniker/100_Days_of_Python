from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import random


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##Cafe TABLE Configuration
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
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random_cafe():
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(cafes)
        return jsonify(cafe={"can_take_calls":random_cafe.can_take_calls,
                   "coffee_price":random_cafe.coffee_price,
                   "has_sockets":random_cafe.has_sockets,
                   "has_toilet":random_cafe.has_toilet,
                   "has_wifi":random_cafe.has_wifi,
                   "id":random_cafe.id,
                   "img_url":random_cafe.img_url,
                   "location":random_cafe.location,
                   "map_url":random_cafe.map_url,
                   "name":random_cafe.name,
                   "seats":random_cafe.seats})

@app.route("/all", methods=["GET"])
def all_cafes():
    with app.app_context():
        shops = db.session.execute(db.select(Cafe)).scalars().all()
        return jsonify(cafes=[cafe.to_dict() for cafe in shops])
    
@app.route("/search")
def search_cafe_location():
    with app.app_context():
        query_location = request.args.get("loc")
        cafe = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalar()
        if cafe:
            return jsonify(cafe.to_dict())
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe_location():
    with app.app_context():
        new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        has_sockets=bool(request.form.get("sockets")),
        can_take_calls=bool(request.form.get("calls")),
        coffee_price=request.form.get("coffee_price"))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    with app.app_context():
        price_to_edit = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if price_to_edit:
            price_to_edit.coffee_price = request.args.get("new_price")
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200
        else:
            return jsonify(response={"error": "Sorry a cafe with that id was not found in the database."}), 404

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    # api_key = "TopSecretAPIKey"
    with app.app_context():
        if api_key == "TopSecretAPIKey":
            cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            if cafe_to_delete:
                db.session.delete(cafe_to_delete)
                db.session.commit()
                return jsonify(response={"success": "Successfully deleted cafe."}), 200
            else:
                return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            return jsonify(error={"Forbidden": "Sorry that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
