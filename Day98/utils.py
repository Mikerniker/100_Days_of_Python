import requests
from moralis import evm_api

# MORALIS_API_KEY = os.getenv("MORALIS_API_KEY")
MORALIS_API_KEY="api_key"


# def get_net_worth():
#     params = {
#         "exclude_spam": True,
#         "exclude_unverified_contracts": true,
#         "max_token_inactivity": 1,
#         "min_pair_side_liquidity_usd": 1000,
#         "address": ""
#     }

#     result = evm_api.wallets.get_wallet_net_worth(
#         api_key=MORALIS_API_KEY,
#         params=params,
#     )

#     return result


def get_token_prices():
   body = {
        "tokens": [
            {"token_address": "0x514910771af9ca656af840dff83e8264ecf986ca"},  # Chainlink
            {"token_address": "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9"},  # Aave
            {"token_address": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0"},  # Matic
        ]
    }
   
   params = {
        "chain": "eth",
        "include": "percent_change"
    }
   
   result = evm_api.token.get_multiple_token_prices(
        api_key=MORALIS_API_KEY,
        body=body,
        params=params,
    )
   
   return result

def check_price(change):
   


