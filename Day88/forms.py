from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Coffee Price', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired(), URL()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    seats = StringField('Seating Capacity', validators=[DataRequired()])
    has_toilet = BooleanField('Has a Toilet')
    has_wifi = BooleanField('Has Wifi')
    has_sockets = BooleanField('Has Outlets')
    can_take_calls = BooleanField('Takes Calls')
    submit = SubmitField('Submit')