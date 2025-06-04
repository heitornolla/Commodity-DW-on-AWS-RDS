import os

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf

load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

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


def save_to_postgres(df, schema='public'):
  df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

  print(f'Saved to {schema}')


if __name__ == "__main__":
  data = get_all_commodity_data()
  save_to_postgres(data, schema='public')