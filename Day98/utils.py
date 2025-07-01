import requests
from moralis import evm_api

# MORALIS_API_KEY = os.getenv("MORALIS_API_KEY")
MORALIS_API_KEY="api_key"


def get_net_worth():
    params = {
        "exclude_spam": True,
        "exclude_unverified_contracts": true,
        "max_token_inactivity": 1,
        "min_pair_side_liquidity_usd": 1000,
        "address": ""
    }

    result = evm_api.wallets.get_wallet_net_worth(
        api_key=MORALIS_API_KEY,
        params=params,
    )

    return result


def get_eth_wallet_balance(addresses):
    pass



def get_sol_wallet_balance(addresses):
    pass



def get_token_prices(symbol):
    pass