from flask import Flask, render_template, request, redirect, url_for, flash, redirect, url_for,\
    session, send_file
from PIL import Image
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'


@app.route("/", methods=["GET", "POST"])
def home():
    # image_colors = get_rgb_final()
    return render_template("index.html", colors=image_colors)


if __name__ == '__main__':
    app.run(debug=True)