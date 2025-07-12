from flask import Flask, render_template, request
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'

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




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)