from flask import Flask, render_template
from moralis import sol_api
import random
import datetime


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




if __name__ == '__main__':
    app.run(debug=True)







