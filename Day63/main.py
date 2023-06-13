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
        data = Books(title=request.form['title'].title(),
                     author=request.form['author'].title(),
                     rating=request.form['rating'].title())
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_rating(book_id):
    book = Books.query.filter_by(id=book_id).first()
    if request.method == 'POST':
        book.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", book=book)


@app.route('/<int:book_id>')
def delete(book_id):
    delete_book_id = book_id
    book_to_delete = Books.query.get(delete_book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
