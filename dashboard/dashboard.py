import os

from dotenv import load_dotenv
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)


def get_data():
    query = f"""
    SELECT
        date,
        symbol,
        closing_price,
        action,
        quantity,
        value,
        earnings
    FROM
        public.dm_commodities;
    """
    try:
        df = pd.read_sql(query, engine)
        return df
    except ProgrammingError as e:
        st.error("Error acessing table")
        return pd.DataFrame()  


st.set_page_config(page_title='Dashboard', layout='wide')


st.title('Commodities Dashboard')


st.write("Data from commodities and their respective transactions")

df = get_data()

if df.empty:
    st.write("Unable to load data")
else:
    st.write("### Data")
    st.dataframe(df)


    st.write("### Summary")
    st.write(df.describe())