from fastapi import FastAPI

import yfinance as yf



app = FastAPI()

@app.get("/stockTicker")
async def getStockPrice(stockTkr):
    stock = yf.Ticker(stockTkr)
    price = stock.info['currentPrice']
    print(price)
    return {"message": "Stock price of " + stockTkr + " is "+ str(price)}
