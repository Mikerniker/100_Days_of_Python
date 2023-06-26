from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
from flask import jsonify
import random


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
