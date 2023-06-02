from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(u'Coffee Rating', choices=[('☕'), ('☕', '☕'), ('☕', '☕', '☕'), ('☕', '☕', '☕', '☕'), ('☕', '☕', '☕', '☕', '☕')], validators=[DataRequired()])
    wifi_rating = SelectField(u'Wifi Rating', choices=[('💪'), ('💪', '💪'), ('💪', '💪', '💪'), ('💪', '💪', '💪', '💪'), ('💪', '💪', '💪', '💪', '💪')], validators=[DataRequired()])
    outlet_rating = SelectField(u'Power Outlet Rating', choices=[('🔌'), ('🔌', '🔌'), ('🔌', '🔌', '🔌'), ('🔌', '🔌', '🔌', '🔌'), ('🔌', '🔌', '🔌', '🔌', '🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')
