from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'
bootstrap = Bootstrap5(app)

@app.route("/", methods=["GET", "POST"])
def home():
    todo_form = TodoForm()
    # search_form = SearchForm()
    if todo_form.validate_on_submit():
        todo_item = request.form.get("todo_item").title()
        due_date = request.form.get("due_date")
        start_time = request.form.get("start_time")
        end_field = request.form.get("end_field")
        status = request.form.get("status")
        print(todo_item, due_date, start_time, end_field, status)
        return render_template("home.html", form=todo_form, todo=todo_item,
                               start = start_time, end = end_field)

    return render_template("home.html", form=todo_form,)