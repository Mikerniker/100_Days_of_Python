from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
from flask import jsonify
import random


app = Flask(__name__)