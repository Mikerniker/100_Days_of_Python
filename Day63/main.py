from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template("index.html", book_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        book_to_add =  {
            "title": request.form['title'],
            "author": request.form['author'],
            "rating": request.form['rating'],
        }

        data = Books(title=book_to_add["title"], author=book_to_add["author"], rating=book_to_add["rating"])
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_rating(book_id):
    book = Books.query.filter_by(id=book_id).first()
    return render_template("edit.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)
