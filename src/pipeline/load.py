import os

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

from pipeline.extract import get_all_commodity_data

load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)


def save_to_postgres_rds(df, schema='public'):
  df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

  print(f'Saved to {schema}')


if __name__ == "__main__":
  data = get_all_commodity_data()
  save_to_postgres_rds(data, schema='public')