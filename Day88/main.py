from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from forms import CafeForm, SearchForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'
bootstrap = Bootstrap5(app)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Configured Cafe Table
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
    

@app.route("/", methods=["GET", "POST"])
def home():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        cafe_loc = request.form.get("search_item").title()
        result = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_loc))
        all_cafes = result.scalars().all()

        if all_cafes:
            flash(f"See cafes in {cafe_loc} below.", 'no_error')
            return render_template("index.html", form=search_form,
                                   cafes=all_cafes, display_result=True)
        else:
            flash("Cafes in this area are not currently available.", 'error')
            return redirect(url_for('home'))

    return render_template("index.html", form=search_form)


@app.route("/cafes")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return render_template('cafes.html', cafes=all_cafes)


@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("has_sockets")),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("price")
            )
        db.session.add(new_cafe)
        db.session.commit()
        flash(f"Successfully added new cafe", 'no_error')
        return redirect(url_for('post_new_cafe'))
    return render_template('add_cafe.html', form=form)


@app.route("/delete/<int:cafe_id>")
def delete_post(cafe_id):
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_cafes'))


@app.route("/edit/<int:cafe_id>", methods=["GET", "POST"])
def edit_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    edit_cafe_form = CafeForm(
        name=cafe.name,
        location=cafe.location,
        price=cafe.coffee_price,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        seats=cafe.seats,
        has_toilet=cafe.has_toilet,
        has_wifi=cafe.has_wifi,
        has_sockets=cafe.has_sockets,
        can_take_calls=cafe.can_take_calls
    )
    if edit_cafe_form.validate_on_submit():
        cafe.name = edit_cafe_form.name.data
        cafe.location = edit_cafe_form.location.data
        cafe.coffee_price = edit_cafe_form.price.data
        cafe.map_url = edit_cafe_form.map_url.data
        cafe.img_url = edit_cafe_form.img_url.data
        cafe.seats = edit_cafe_form.seats.data
        cafe.has_wifi = edit_cafe_form.has_wifi.data
        cafe.has_toilet = edit_cafe_form.has_toilet.data
        cafe.has_sockets = edit_cafe_form.has_sockets.data
        cafe.can_take_calls = edit_cafe_form.can_take_calls.data
        db.session.commit()
        return redirect(url_for("get_all_cafes"))
    return render_template("add_cafe.html", form=edit_cafe_form, is_edit=True)


if __name__ == '__main__':
    app.run(debug=True)