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
   
   
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)






# params = {
#   "nft_metadata": True,
#   "media_items": False,
#   "exclude_spam": False,
#   "network": "mainnet",
#   "address": COLLECTION_ADDRESS
# }

# result = sol_api.account.get_nfts(
#   api_key=api_key,
#   params=params,
# )

# print(result)
