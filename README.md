# Crypto_Update_Notion_Database

This project involves retrieving and updating cryptocurrency data using the Notion API. The code is written in Python and uses the `requests`, `database`, `os`, and `dotenv` libraries.

## Getting Started

1. Clone this repository to your local machine.
2. Set up your environment variables by creating a `.env` file and adding your Notion secret key:

NOTION_SECRET=your_secret_key_here

3. Install the required libraries using `pip`:

```
pip install requests database os dotenv
```

1. Run the script index.py to fetch cryptocurrency data from your Notion database and update relevant properties.

# Usage
The script uses the provided secret key and database IDs to retrieve cryptocurrency data and update your Notion pages accordingly. The data includes information such as the current price, price in BTC, and percentage changes over different time intervals.

# How It Works

The script makes a POST request to the Notion API to query the specified database.
For each page in the response, it extracts the cryptocurrency code and fetches additional data from the CoinMarketCap API.
The fetched data is used to construct a JSON object to update the Notion page's properties.
Please note that you should have a valid Notion API integration set up and ensure that your environment variables are correctly configured.

# Resources

Notion API Documentation: https://developers.notion.com/docs
CoinMarketCap API: https://coinmarketcap.com/api/documentation
#Disclaimer

This project is for educational purposes and may require adjustments to fit your specific use case. Use it responsibly and follow API usage guidelines.

Feel free to reach out if you have any questions or need further assistance!
