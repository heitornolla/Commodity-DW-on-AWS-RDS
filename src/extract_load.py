import os

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf


def get_commodity_data(ticker, period='5d', interval='1d'):
  ticker = yf.Ticker(ticker)
  data = ticker.history(period=period, interval=interval)[['Close']]
  data['symbol'] = ticker
  return data


def get_all_commodity_data(commodities):
  data = []
  for symbol in commodities:
    data.append(get_commodity_data(symbol))

  return pd.concat(data)


if __name__ == "__main__":
  commodities = ['CL=F', 'GC=F', 'SI=F']
  data = get_all_commodity_data(commodities)
  print(data)