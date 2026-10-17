import os
from os import name

import requests
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient


#---------------------------------- Global Variables -------------------------------------
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

#test
stop_price = 0
take_profit = 0

#------------------------------------- Account -------------------------------------------
def get_account():
    pass

def get_assets():
    pass

#------------------------------------- Orders -------------------------------------------
#TODO: update to take inputs
def create_order():
    new_order = requests.post(
        f"{BASE_URL}/orders",
        headers=headers,
        json={
            "time_in_force": "day",
            "type": "market",
            "side": "buy",
            "symbol": "TSLA",
            "qty": "1",
            "stop_loss": {stop_price},
            "take_profit": {take_profit}
        },)

    new_order.raise_for_status()
    return new_order

def delete_order():
    pass

#------------------------------------ Positions ----------------------------------------
def all_open_position():
    positions = requests.get(
        f"{BASE_URL}/positions",
        headers=headers
    )

    positions.raise_for_status()
    return positions

def close_position():
    close_order = requests.delete(
        f"{BASE_URL}/positions/symbol_or_asset_id",
        headers=headers,
        json={
            "symbol": "TSLA",
            "qty": 1
        },)

    close_order.raise_for_status()
    return close_order

#------------------------------------ Watchlist ----------------------------------------
#TODO: update to take inputs
def create_watchlist():
    new_watchlist = requests.post(
        f"{BASE_URL}/watchlists",
        headers=headers,
        json={
            "name": "La poderosa",
            "symbols": ["AAPL", "MSFT", "NVDA", "AMZN", "META"]
        },)

    new_watchlist.raise_for_status()
    return new_watchlist.json()

def add_symbol():
    new_symbol = requests.post(
        f"{BASE_URL}/watchlists/{watchlist_id}",
        headers=headers,
        json={
            "symbol": "TSLA"
        },)

    new_symbol.raise_for_status()
    return new_symbol.json()

def delete_symbol():
    delete_asset = requests.delete(
        f"{BASE_URL}/watchlists/{watchlist_id}/AAPL",
        headers=headers,
        )

    delete_asset.raise_for_status()
    return delete_asset

def get_whole_watchlist():
    watchlist = requests.get(
        f"{BASE_URL}/watchlists/{watchlist_id}",
        headers=headers,
        )

    return watchlist.text

#TODO: complete
def delete_watchlist():
    pass

def save_watchlist_details():
    pass

data = get_whole_watchlist()

print(data)