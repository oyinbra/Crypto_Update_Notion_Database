import requests
import notion
import os
from dotenv import load_dotenv
load_dotenv()


# import pprint

headers = {
    'X-CMC_PRO_API_KEY': os.environ.get("CMC_API"),
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '1000',
    # 'start' : '1001',
    # 'limit' : '2000',
    'convert': 'usd'
}

secret = os.environ.get("NOTION_SECRET")
base_db_url = "https://api.notion.com/v1/databases/"
base_pg_url = "https://api.notion.com/v1/pages/"
base_crypto_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

wallet_db_id = notion.portfolio
data = {}
header = {"Authorization": secret, "Notion-Version": "2021-05-13", "Content-Type": "application/json"}

response = requests.post(base_db_url + wallet_db_id + "/query", headers=header, data=data)

json = requests.get(base_crypto_url, params=params, headers=headers).json()

coins = json['data']

for x in coins:
    symbol = x['symbol']
    price = x['quote']['USD']['price']
    data = {
        "query": {
            "and": [                {                    "property": "symbol",                    "equals": symbol                }            ]
        }
    }
    response = requests.post(base_db_url + wallet_db_id + "/query", headers=header, json=data)
    result = response.json()
    if result['results']:
        page_id = result['results'][0]['id']
        update_data = {
            "price_usd": {
                "number": price
            }
        }
        requests.patch(base_pg_url + page_id, headers=header, json=update_data)
