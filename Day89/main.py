from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from forms import TodoForm
from datetime import datetime
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'
bootstrap = Bootstrap5(app)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Configured Cafe Table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_item = db.Column(db.String(250), nullable=False)
    due_date = db.Column(db.Date())
    start_time = db.Column(db.Time())
    end_field = db.Column(db.Time())
    status = db.Column(db.String(250))

# with app.app_context():
#     db.create_all()



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




if __name__ == '__main__':
    app.run(debug=True)