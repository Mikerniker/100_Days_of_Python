from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", book_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        book_to_add =  {
            "title": request.form['title'],
            "author": request.form['author'],
            "rating": request.form['rating'],
        }
        all_books.append(book_to_add)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
