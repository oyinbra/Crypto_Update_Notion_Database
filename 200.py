import requests
import notion
import os
from dotenv import load_dotenv
load_dotenv()
secret = os.environ.get("NOTION_SECRET")
wallet_db_id = notion.crypto
base_crypto_url = notion.top200
base_db_url = "https://api.notion.com/v1/databases/"
base_pg_url = "https://api.notion.com/v1/pages/"

data = {}
header = {"Authorization": secret, "Notion-Version": "2021-05-13",
          "Content-Type": "application/json"}

response = requests.post(base_db_url + wallet_db_id +
                         "/query", headers=header, data=data)

for page in response.json()["results"]:
    page_id = page["id"]
    props = page['properties']
    if 'Type' not in props:
        print("Error: 'Type' property is missing in the page.")
        continue
    if props['Type']['type'] != 'select':
        print("Error: 'Type' property is not of the type 'select'.")
        continue
    if props['Type']['select']['name'] != 'Crypto':
        print("Error: 'Type' is not 'Crypto'.")
        continue
    if 'Code' not in props:
        print("Error: 'Code' property is missing in the page.")
        continue
    if props['Code']['type'] != 'rich_text':
        print("Error: 'Code' property is not of the type 'rich_text'.")
        continue
    try:
        asset_code = props['Code']['rich_text'][0]['plain_text']
    except IndexError:
        print("Error: 'rich_text' list is empty.")
        continue
    request_by_code = requests.get(base_crypto_url).json()['data']
    coin = next(
        (item for item in request_by_code if item["symbol"] == asset_code), None)
    if coin:
        price = coin['price_usd']
        price_btc = coin['price_btc']
        pcent_1h = coin['percent_change_1h']
        pcent_24h = coin['percent_change_24h']
        pcent_7days = coin['percent_change_7d']
        coin_url = "https://coinmarketcap.com/currencies/" + coin['nameid']
        data_price = '{"properties":   \
                            {"Price": { "number":' + str(price) + '},\
                            "price btc": { "number":' + str(price_btc) + '}, \
                            "% 1H": { "number":' + str(pcent_1h) + '}, \
                            "% 24H": { "number":' + str(pcent_24h) + '}, \
                            "% 7days": { "number":' + str(pcent_7days) + '}, \
                            "URL": { "url":"' + coin_url + '"}}}'

        if not props.get('Price'):
            send_price = requests.patch(
                base_pg_url + page_id, headers=header, data=data_price)
