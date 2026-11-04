#TODO: update to use args and kwargs if possible and better
def builder(time, order_type, side, symbol, qty, stop_price, profit_price):
    i = {
        "time_in_force": {time},
        "type": {order_type},
        "side": {side},
        "symbol": {symbol},
        "qty": {qty},
        "stop_loss": {stop_price},
        "take_profit": {profit_price}
    }

    return i