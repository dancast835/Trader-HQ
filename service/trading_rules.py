from backend.API.alpaca_trading import *

def position_size(funds_available, num_of_positions, current_price):
    #money per position = divide number of positions from capital
    funds_per_position = funds_available / num_of_positions
    #position size = divide  current price per asset from money per position
    trade_size =  round(funds_per_position / current_price, 1)

    return trade_size

def calculate_stop_loss(order_type, percentage, current_price):
    #get current price / price bought
    #get info from database for stop percentage
    percentage = percentage / 100
    price_difference = current_price * percentage

    if order_type == "Long":
        stop_loss = int(current_price + price_difference)

    elif order_type == "Short":
        stop_loss = int(current_price - price_difference)

    else:
        return False

    return stop_loss

def calculate_take_profit(order_type, percentage, current_price):
    # get current price / price bought
    #get info from database for percentage
    percentage = percentage / 100
    price_difference = current_price * percentage

    if order_type == "Long":
        profit_price = int(current_price + price_difference)

    elif order_type == "Short":
        profit_price = int(current_price - price_difference)

    else:
        return False

    return profit_price
