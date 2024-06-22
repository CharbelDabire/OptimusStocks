# stocks/services/stock_service.py

import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si
from yahoo_fin import options
from yahoo_fin import news
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies

class StockService:
    def __init__(self, alpha_vantage_api_key):
        self.alpha_vantage_api_key = alpha_vantage_api_key
        self.ts = TimeSeries(key=alpha_vantage_api_key)
        self.fd = FundamentalData(key=alpha_vantage_api_key)
        self.ti = TechIndicators(key=alpha_vantage_api_key)
        self.sp = SectorPerformances(key=alpha_vantage_api_key)
        self.cc = CryptoCurrencies(key=alpha_vantage_api_key)

    def get_yahoo_fin_info(self, ticker):
        try:
            return si.get_quote_table(ticker)
        except Exception as e:
            print(f"Error fetching Yahoo Finance data: {e}")
            return None

    def get_yfinance_info(self, ticker):
        try:
            stock = yf.Ticker(ticker)
            return stock.info
        except Exception as e:
            print(f"Error fetching yfinance data: {e}")
            return None

    def get_alpha_vantage_info(self, ticker):
        try:
            data, _ = self.ts.get_quote_endpoint(ticker)
            return data
        except Exception as e:
            print(f"Error fetching Alpha Vantage data: {e}")
            return None

    def get_stock_news(self, ticker):
        try:
            return news.get_yf_rss(ticker)
        except Exception as e:
            print(f"Error fetching stock news: {e}")
            return None

    def get_stock_options(self, ticker):
        try:
            return options.get_options_chain(ticker)
        except Exception as e:
            print(f"Error fetching stock options: {e}")
            return None

    def get_fundamental_data(self, ticker):
        try:
            data, _ = self.fd.get_company_overview(ticker)
            return data
        except Exception as e:
            print(f"Error fetching fundamental data: {e}")
            return None

    def get_technical_indicators(self, ticker, indicator):
        try:
            data, _ = self.ti.get_technical_indicator(ticker, indicator)
            return data
        except Exception as e:
            print(f"Error fetching technical indicators: {e}")
            return None

    def get_sector_performance(self):
        try:
            data, _ = self.sp.get_sector()
            return data
        except Exception as e:
            print(f"Error fetching sector performance: {e}")
            return None

    def get_crypto_data(self, symbol):
        try:
            data, _ = self.cc.get_digital_currency_daily(symbol)
            return data
        except Exception as e:
            print(f"Error fetching crypto data: {e}")
            return None
