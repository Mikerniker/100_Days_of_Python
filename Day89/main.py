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


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        print(name, email, password)
        return redirect(url_for('register'))
            # db.session.add(new_todo)
            # db.session.commit()
    return render_template("register.html", form=register_form)



@app.route("/mytodo", methods=["GET", "POST"])
def mytodo():
    todo_form = TodoForm()
    todos = get_all_todos()
    # search_form = SearchForm()
    if todo_form.validate_on_submit():
        due_date_str = request.form.get("due_date")
        due_date = datetime.strptime(due_date_str,
                                     '%Y-%m-%d').date() if due_date_str else None

        start_time_str = request.form.get("start_time")
        start_time = datetime.strptime(start_time_str,
                                       '%H:%M').time() if start_time_str else None

        end_field_str = request.form.get("end_field")
        end_field = datetime.strptime(end_field_str,
                                      '%H:%M').time() if end_field_str else None

        new_todo = Todo(
            todo_item=request.form.get("todo_item"),
            due_date=due_date,
            start_time=start_time,
            end_field=end_field,
            status=request.form.get("status"))

        try:
            db.session.add(new_todo)
            db.session.commit()

            todos = get_all_todos()
            return redirect(url_for('mytodo'))

        except IntegrityError:
            db.session.rollback()
            flash('Todo item already exists.', 'error')
            return redirect(url_for('mytodo'))

    return render_template("todo.html", form=todo_form, todos=todos)

def get_all_todos():
    result = db.session.execute(db.select(Todo))
    all_todos = result.scalars().all()
    return all_todos


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    todo_to_delete = db.get_or_404(Todo, todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('mytodo'))


if __name__ == '__main__':
    app.run(debug=True)