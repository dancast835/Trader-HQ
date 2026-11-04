import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets/v2"

watchlist_id = os.getenv("WATCHLIST_ID")
account_id = os.getenv("ACCOUNT_ID")

headers = {
    "APCA-API-KEY-ID": api_key,
    "APCA-API-SECRET-KEY": secret_key,
    "accept": "application/json",
    "content-type": "application-json"
}

def current_price(symbol):
    response = requests.get(
        url=f"{BASE_URL}/stocks/quotes/latest",
        headers=headers,
        json={
            "symbol": {symbol}
        })

    response.raise_for_status()

    return response