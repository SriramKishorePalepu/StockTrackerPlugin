from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
async def defaultRoute():
    return {"message": "Please update the url and include /currentstockprice/ \"Name of the company\" e.g. /currentstockprice/tsla and press enter"}

@app.get("/currentstockprice/{stockTicker}")
async def getCurrentStockPriceUsingStockTicker(stockTicker : str):
    stock = yf.Ticker(stockTicker)
    price = stock.info['currentPrice']
    stockLongName = stock.info['longName']
    return {"message": "Stock price of " + stockLongName + " is "+ str(price)}
