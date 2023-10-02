from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/stockTicker")
async def root(stockTkr):
    stock = yf.Ticker(stockTkr)
    price = stock.info['currentPrice']
    stockLongName = stock.info['longName']
    return {"message": "Stock price of " + stockLongName + " is "+ str(price)}
