from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, DateTimeField, DateField, TimeField
from wtforms.validators import DataRequired, URL

class TodoForm(FlaskForm):
    todo_item = StringField(label='To Do',
                              validators=[DataRequired()],
                              render_kw={"placeholder": "Add a To Do"})
    due_date = DateField('Due date')
    start_time = TimeField("Start")
    end_field = TimeField("End Time")
    status = SelectField(u'Status', validators=[DataRequired()], choices=[('To Do'), ('Doing'), ('Done')])
    submit = SubmitField('Submit')