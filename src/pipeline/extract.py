import pandas as pd
import yfinance as yf

commodities = ['CL=F', 'GC=F', 'SI=F']


def get_commodity_data(symbol, period='5d', interval='1d'):
  ticker = yf.Ticker(symbol)
  dados = ticker.history(period=period, interval=interval)[['Close']]
  dados['symbol'] = symbol  
  return dados


def get_all_commodity_data():
  dataframe = []
  for symbol in commodities:
      data = get_commodity_data(symbol)
      dataframe.append(data)
  return pd.concat(dataframe)