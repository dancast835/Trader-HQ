from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins =["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")

def home():
    return {"message": "Trader HQ"}

@app.get("/greetings")
def greetings():
    return {"message": "Hello React"}

#------------------------------------- Display -------------------------------------------
def account_details():
    pass

    #display account details like balance, etc...

def strategies():
    pass

    #display strategies and rules

def trade_history():
    pass

    #get data from database to display stats from account

def trading_news():
    pass

    #display current news for specific stocks from api

def trading_view_access():
    pass

    #provide access to tradingview charts for selected stock

def send_positions():
    pass

    #display recent positions

def manage_watchlist():
    pass

    #manage and display watchlist

#------------------------------------- Orders -------------------------------------------
def send_order():
    pass

    #call strategy, get data and pass it to order builder

    #call order_builder to organize JSON from strategies

    #call create_order from alpaca_trading.py and pass in JSON from order builder

def close_order():
    pass





if __name__ == "__backend__":
    uvicorn.run("backend:app", reload=True)
