from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, EmailField, PasswordField, BooleanField, DateTimeField, DateField, TimeField
from wtforms.validators import DataRequired, URL

class TodoForm(FlaskForm):
    todo_item = StringField(label='To Do',
                              validators=[DataRequired()],
                              render_kw={"placeholder": "Add a To Do"})
    due_date = DateField('Due date')
    start_time = TimeField("Start")
    end_field = TimeField("End Time")
    status = SelectField(u'Schedule', validators=[DataRequired()], choices=[('Today'), ('Tomorrow'), ('Upcoming')])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    name = StringField(label="Name", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField('Sign Me Up')


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField('Login')
