from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from forms import TodoForm, RegisterForm, LoginForm
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'
bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Configured Todo Table
class Todo(db.Model):
    __tablename__ = "all_todos"  #new
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    owner = relationship("User", back_populates="todos")
    todo_item = db.Column(db.String(250), nullable=False)
    due_date = db.Column(db.Date())
    start_time = db.Column(db.Time())
    end_field = db.Column(db.Time())
    status = db.Column(db.String(250))



class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    todos = relationship("Todo", back_populates="owner")  # added


@login_manager.user_loader
def load_user(id):
    user_id = db.session.execute(db.select(User).where(User.id == id)).scalar()
    return user_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.execute(
            db.select(User).where(User.email == email)).scalar()
        if not user:
            flash('This email does not exist. Please try again.', 'error')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.', 'error')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('mytodo'))
    return render_template('login.html', form=form, logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        email = request.form.get('email')
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            flash("You've already signed up with that email, log in instead!", 'error')
            return redirect(url_for('login'))


        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(name=request.form.get("name"),
                        email=request.form.get("email"),
                        password=hash_and_salted_password,)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for('mytodo'))
    return render_template("register.html", form=register_form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", logged_in=current_user.is_authenticated)


@app.route("/mytodo", methods=["GET", "POST"])
@login_required
def mytodo():
    todo_form = TodoForm()
    todos = get_all_todos()
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
            status=request.form.get("status"),
            owner_id=current_user.id,
            owner=current_user,)

        try:
            db.session.add(new_todo)
            db.session.commit()

            todos = get_all_todos()
            return redirect(url_for('mytodo'))

        except IntegrityError:
            db.session.rollback()
            flash('Todo item already exists.', 'error')
            return redirect(url_for('mytodo'))
    return render_template("todo.html", form=todo_form, todos=todos, current_user=current_user))


def get_all_todos():
    if current_user.is_authenticated:
        user_todos = Todo.query.filter_by(owner_id=current_user.id)
        return user_todos
    else:
        return []


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    todo_to_delete = db.get_or_404(Todo, todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('mytodo'))


@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit_todo(todo_id):
    todo_to_edit = db.get_or_404(Todo, todo_id)
    print(todo_id)
    edit_todo_form = TodoForm(
        todo_item=todo_to_edit.todo_item,
        due_date=todo_to_edit.due_date,
        start_time=todo_to_edit.start_time,
        end_field=todo_to_edit.end_field,
        status=todo_to_edit.status)

    if edit_todo_form.validate_on_submit():
        todo_to_edit.todo_item = edit_todo_form.todo_item.data
        todo_to_edit.due_date = edit_todo_form.due_date.data
        todo_to_edit.start_time = edit_todo_form.start_time.data
        todo_to_edit.end_field = edit_todo_form.end_field.data
        todo_to_edit.status = edit_todo_form.status.data

        db.session.commit()
        return redirect(url_for("mytodo"))
    return render_template("edit_todo.html", form=edit_todo_form, 
                           is_edit=True, current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True)