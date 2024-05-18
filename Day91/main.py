from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)