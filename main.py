from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
async def defaultRoute():
    return {"message": "Please update the url and include /stockTicker/ \"Name of the company\" e.g. /stockTicker/tsla and press enter"}

@app.get("/currentstockprice/{stockTkr}")
async def getCurrentStockPriceUsingStockTicker(stockTicker : str):
    stock = yf.Ticker(stockTicker)
    price = stock.info['currentPrice']
    stockLongName = stock.info['longName']
    return {"message": "Stock price of " + stockLongName + " is "+ str(price)}
