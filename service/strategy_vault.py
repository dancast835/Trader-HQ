from shlex import quote

from trading_rules import *
from backend.API.alpaca_trading import *
from backend.API.alpaca_market_data import *
from backend.backend import *
from service.order_builder import *
import random

def up_and_down():
    funds = 1000
    #get 3 symbols to trade from trading rules available_symbols
    open_positions = []
    symbols = []
    sl_percentage = 1
    tp_percentage = 5


    # get all open positions from api
    positions = all_open_position()
    for i in positions:
        open_positions.append(i["symbol"])

    # check watchlist and create a list but remove the stocks that have an open order
    watchlist = get_whole_watchlist()
    for i in watchlist["assets"]:
        symbols.append(i["symbol"])

    # remove open_position assets from symbol available list to trade
    for i in symbols:
        if i in open_positions:
            symbols.remove(i)

    # randomly select 3 stocks each trading day
    selected_symbols = random.sample(symbols, 3)
    qty_positions = len(selected_symbols) * 2

    for long in selected_symbols:
        #calculate trade size from trading rules for each symbol
        ask_price =current_price(long)["quotes"][long]["ap"]
        qty = position_size(funds, qty_positions, ask_price)

        #calculate stop loss / take profit and trailing stop from lastest price for 3 long positions and 3 short positions
        stop_price = calculate_stop_loss("Long", sl_percentage, ask_price)
        profit_price = calculate_take_profit("Long", tp_percentage, ask_price)

        #order builder
        order = builder(time="gtc", order_type="market", side="buy", symbol=long, qty=qty, stop_price=stop_price, profit_price=profit_price)

        place_order(order)

    for short in selected_symbols:
        #calculate trade size from trading rules for each symbol
        ask_price = current_price(short)["quotes"][short]["ap"]
        qty = position_size(funds, qty_positions, ask_price)

        #calculate stop loss / take profit and trailing stop from lastest price for 3 long positions and 3 short positions
        stop_price = calculate_stop_loss("Short", sl_percentage, ask_price)
        profit_price = calculate_take_profit("Short", tp_percentage, ask_price)

        #order builder
        order = builder(time="gtc", order_type="market", side="buy", symbol=short, qty=qty, stop_price=stop_price, profit_price=profit_price)

        place_order(order)

    return