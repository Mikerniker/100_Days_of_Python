from flask import Flask, render_template, request
import requests

from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'


class BtcAlert(FlaskForm):
    user_choice = SelectField(u'Price Direction', choices=[("up", "Above 🢁"),("down", "Below 🡻")])
    price = IntegerField('BTC_Price')

def get_btc_details():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    response = requests.get(url)
    data = response.json()

    info = {
        "name": data["name"],
        "symbol": data["symbol"],
        "logo": data["image"]["large"],
        "current_price": data["market_data"]["current_price"]["usd"],
        "price_change_24h": data["market_data"]["price_change_percentage_24h"],
    }

    return info


@app.route("/", methods=['GET', 'POST'])
def home():
    form = BtcAlert()
    result = get_btc_details()
    return render_template("index.html", data=result, form=form))


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)