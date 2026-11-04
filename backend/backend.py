import uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.strategy_vault import *
from service.scheduler import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_scheduler()
    scheduler.start()

    print("Trader HQ scheduler started")

    yield

    scheduler.shutdown(wait=False)
    print("Trader HQ scheduler stopped")
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins =["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#------------------------------------- Orders -------------------------------------------
def place_order(order):
    create_order(order)

def close_order():
    pass


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

def all_open_positions():
    pass

    #display recent positions

def manage_watchlist():
    pass

    #manage and display watchlist





if __name__ == "__backend__":
    uvicorn.run("backend:app", reload=True)
