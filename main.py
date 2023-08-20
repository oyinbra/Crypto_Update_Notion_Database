# Import necessary modules
import os
import database
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the secret from environment variables
secret = os.environ.get("NOTION_SECRET")

# Define database IDs and URLs
wallet_db_id = database.watchlist
base_crypto_url = database.top0100
base_db_url = "https://api.notion.com/v1/databases/"
base_pg_url = "https://api.notion.com/v1/pages/"

# Initialize data dictionary and header for API requests
data = {}
header = {
    "Authorization": secret,
    "Notion-Version": "2021-05-13",
    "Content-Type": "application/json",
}

# Send a POST request to get wallet data
response = requests.post(
    base_db_url + wallet_db_id + "/query", headers=header, data=data
)

# Loop through the pages in the response
for page in response.json()["results"]:
    page_id = page["id"]
    props = page["properties"]

    # Check if 'Code' property exists in the page
    if "Code" not in props:
        print("Error: 'Code' property is missing in the page.")
        continue
    
    try:
        # Get the asset code from the 'Code' property
        asset_code = props["Code"]["rich_text"][0]["plain_text"]
    except IndexError:
        print("Error: 'rich_text' list is empty.")
        continue

    # Send a GET request to get cryptocurrency data
    request_by_code = requests.get(base_crypto_url).json()["data"]
    
    # Find the coin with matching symbol in the response
    coin = next(
        (item for item in request_by_code if item["symbol"] == asset_code), None
    )
    
    if coin:
        # Extract relevant coin data
        price = coin["price_usd"]
        price_btc = coin["price_btc"]
        pcent_1h = coin["percent_change_1h"]
        pcent_24h = coin["percent_change_24h"]
        pcent_7days = coin["percent_change_7d"]
        coin_url = "https://coinmarketcap.com/currencies/" + coin["nameid"]
        
        # Prepare JSON data for updating the page
        data_price = (
            '{"properties":   \
                            {"Price": { "number":'
            + str(price)
            + '},\
                            "price btc": { "number":'
            + str(price_btc)
            + '}, \
                            "% 1H": { "number":'
            + str(pcent_1h)
            + '}, \
                            "% 24H": { "number":'
            + str(pcent_24h)
            + '}, \
                            "% 7days": { "number":'
            + str(pcent_7days)
            + '}, \
                            "URL": { "url":"'
            + coin_url
            + '"}}}'
        )

        # Check if 'Price' property exists, then send a PATCH request to update data
        if not props.get("Price"):
            send_price = requests.patch(
                base_pg_url + page_id, headers=header, data=data_price
            )

