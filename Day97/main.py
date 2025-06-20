from flask import Flask, render_template, redirect, session
from moralis import sol_api
import random
import datetime
import stripe



api_key = "MY_MORALIS_API_KEY"
CHAIN = "solana"
COLLECTION_ADDRESS ="*********************"

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(30, 40)
    current_year = datetime.datetime.now().year
   
    return render_template("index.html",
                           price=random_number,
                           year=current_year)


def get_wallet_nft():
    params = {
      "nft_metadata": True,
      "media_items": False,
      "exclude_spam": False,
      "network": "mainnet",
      "address": COLLECTION_ADDRESS
    }

    result = sol_api.account.get_nfts(
      api_key=api_key,
      params=params,
    )
    
    nft_list = []
    
    for nft in result[:12]:
      params = {
        "network": "mainnet",
        "address": nft['mint']
        }

      nft_result = sol_api.nft.get_nft_metadata(
          api_key=api_key,
          params=params,
        )
      
      nft_list.append({
          "name": nft_result["name"],
          "symbol": nft_result["symbol"],
          "url": nft_result["imageOriginalUrl"]
      })

    # print(nft_list)
    return nft_list


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/checkout/<int:index>', methods=['GET', 'POST'])
def checkout(index):
    checkout_item = None
    for nft in nft_data:
        if nft["id"] == index:
            checkout_item = nft
    return render_template('checkout.html',
                           checkout_nft=checkout_item,
                           sol_to_usd = convert_sol)

nft_data = get_wallet_nft()


if __name__ == '__main__':
    app.run(debug=True)







