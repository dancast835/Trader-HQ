import os
from alpaca.trading.client import TradingClient

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")


client = TradingClient(api_key, secret_key, paper=True)

account = client.get_account()

print(account.buying_power)


