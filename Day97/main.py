# from flask import Flask


# app = Flask(__name__)





# if __name__ == '__main__':
#     app.run(debug=True)


from moralis import sol_api


api_key = "MY_MORALIS_API_KEY"
CHAIN = "solana"
COLLECTION_ADDRESS ="*********************"

params = {
  "nft_metadata": True,
  "media_items": False,
  "exclude_spam": False,
  "network": "mainnet",
  "address": COLLECTION_ADDRESS
}