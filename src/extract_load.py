import os

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf

commodities = ['CL=F', 'GC=F', 'SI=F']

def buscas_dados(ticker, periodo='5d', intervalo='1d'):
  ticker = yf.Ticker(ticker)