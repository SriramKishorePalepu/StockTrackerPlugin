from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
async def defaultRoute():
    return {"message": "Please update the url and include /stockTicker/ \"Name of the company\" e.g. /stockTicker/tsla and press enter"}

@app.get("/stockTicker/{stockTkr}")
async def root(stockTkr):
    stock = yf.Ticker(stockTkr)
    price = stock.info['currentPrice']
    stockLongName = stock.info['longName']
    return {"message": "Stock price of " + stockLongName + " is "+ str(price)}
