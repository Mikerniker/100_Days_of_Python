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


def get_token_prices():
    body = {
        "tokens": [
            {
                "token_address": "0xdac17f958d2ee523a2206206994597c13d831ec7"
            },
            {
                "token_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
            },
            {
                "exchange": "uniswapv2",
                "token_address": "0xae7ab96520de3a18e5e111b5eaab095312d7fe84",
                "to_block": "16314545"
            },
            {
                "token_address": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0"
            }
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

result = get_token_prices()
# print(result)
for i in result:
    # print(type(i))
    print(i['usdPrice'])
    print(i['tokenName'])
    print(i['tokenSymbol'])
    print(i['tokenLogo'])

