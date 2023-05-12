from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("guess.html")

@app.route("/guess/<name>")
def check_name(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    age_of_name = data["age"]

    response2 = requests.get(url=f"https://api.genderize.io?name={name}")
    response2.raise_for_status()
    data2 = response2.json()
    gender_of_name = data2["gender"]

    return render_template("names.html", name=name.title(), age=age_of_name, gender=gender_of_name)


if __name__ == "__main__":
    app.run(debug=True)
