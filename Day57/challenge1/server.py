from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("guess.html")

@app.route("/guess/<name>")
def check_name(name):
    def age_gender(url_to_check):
        response = requests.get(url=url_to_check)
        response.raise_for_status()
        data = response.json()
        return data

    genderize_url = f"https://api.genderize.io?name={name}"
    agify_url = f"https://api.agify.io?name={name}"
    gender_of_name = age_gender(genderize_url)["gender"]
    age_of_name = age_gender(agify_url)["age"]

    return render_template("names.html", name=name.title(), age=age_of_name, gender=gender_of_name)


if __name__ == "__main__":
    app.run(debug=True)
