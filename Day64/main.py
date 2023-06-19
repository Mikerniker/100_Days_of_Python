from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_TOKEN = "***********************************"


app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()

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

class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your Rating out of 10 e.g.7.5')
    review = StringField(label='Your Review')
    submit = SubmitField(label="Done")

class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Add movie")

@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating.desc())
    for index, movie_rank in enumerate(all_movies, 1):
        movie_rank.ranking = index
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<movie_title>", methods=["GET", "POST"])
def edit_rating(movie_title):
    form = RateMovieForm()
    movie_to_edit = db.session.execute(db.select(Movie).where(Movie.title == movie_title)).scalar()
    if form.validate_on_submit():
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie_to_edit)


@app.route('/<int:movie_id>')
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        results = find_movie(movie_title)["results"]
        return render_template("select.html", movies=results)
    return render_template("add.html", form=form)

def find_movie(movie):
    parameters = {
        "query": movie,
        "include_adult": False,
        "language": "en-US",
        "page": 1,
    }
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data


@app.route('/add_selected/<int:movie_id>', methods=["GET", "POST"])
def add_selected_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    movie_data = Movie(title=data["title"].title(),
                 img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}",
                 year=data["release_date"].split("-")[0],
                 description=data["overview"])
    db.session.add(movie_data)
    db.session.commit()
    return redirect(url_for('edit_rating', movie_title=data["title"]))


if __name__ == '__main__':
    app.run(debug=False)
