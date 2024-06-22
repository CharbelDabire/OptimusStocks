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

    #Yahoo Fin Service
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

    
    def get_analysts_info(self, ticker):
        try:
            return si.get_analysts_info(ticker)
        except Exception as e:
            print(f"Error fetching analysts info: {e}")
            return None

    def get_balance_sheet(self, ticker):
        try:
            return si.get_balance_sheet(ticker)
        except Exception as e:
            print(f"Error fetching balance sheet: {e}")
            return None

    def get_cash_flow(self, ticker):
        try:
            return si.get_cash_flow(ticker)
        except Exception as e:
            print(f"Error fetching cash flow: {e}")
            return None

    def get_company_info(self, ticker):
        try:
            return si.get_company_info(ticker)
        except Exception as e:
            print(f"Error fetching company info: {e}")
            return None

    def get_currencies(self):
        try:
            return si.get_currencies()
        except Exception as e:
            print(f"Error fetching currencies: {e}")
            return None

    def get_data(self, ticker, start_date=None, end_date=None, index_as_date=True):
        try:
            return si.get_data(ticker, start_date=start_date, end_date=end_date, index_as_date=index_as_date)
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def get_day_gainers(self):
        try:
            return si.get_day_gainers()
        except Exception as e:
            print(f"Error fetching day gainers: {e}")
            return None

    def get_day_losers(self):
        try:
            return si.get_day_losers()
        except Exception as e:
            print(f"Error fetching day losers: {e}")
            return None

    def get_day_most_active(self):
        try:
            return si.get_day_most_active()
        except Exception as e:
            print(f"Error fetching day most active: {e}")
            return None

    def get_dividends(self, ticker):
        try:
            return si.get_dividends(ticker)
        except Exception as e:
            print(f"Error fetching dividends: {e}")
            return None

    def get_earnings(self, ticker):
        try:
            return si.get_earnings(ticker)
        except Exception as e:
            print(f"Error fetching earnings: {e}")
            return None

    def get_earnings_for_date(self, date):
        try:
            return si.get_earnings_for_date(date)
        except Exception as e:
            print(f"Error fetching earnings for date: {e}")
            return None

    def get_earnings_in_date_range(self, start_date, end_date):
        try:
            return si.get_earnings_in_date_range(start_date, end_date)
        except Exception as e:
            print(f"Error fetching earnings in date range: {e}")
            return None

    def get_earnings_history(self, ticker):
        try:
            return si.get_earnings_history(ticker)
        except Exception as e:
            print(f"Error fetching earnings history: {e}")
            return None

    def get_financials(self, ticker):
        try:
            return si.get_financials(ticker)
        except Exception as e:
            print(f"Error fetching financials: {e}")
            return None

    def get_futures(self):
        try:
            return si.get_futures()
        except Exception as e:
            print(f"Error fetching futures: {e}")
            return None

    def get_holders(self, ticker):
        try:
            return si.get_holders(ticker)
        except Exception as e:
            print(f"Error fetching holders: {e}")
            return None

    def get_income_statement(self, ticker):
        try:
            return si.get_income_statement(ticker)
        except Exception as e:
            print(f"Error fetching income statement: {e}")
            return None

    def get_live_price(self, ticker):
        try:
            return si.get_live_price(ticker)
        except Exception as e:
            print(f"Error fetching live price: {e}")
            return None

    def get_market_status(self):
        try:
            return si.get_market_status()
        except Exception as e:
            print(f"Error fetching market status: {e}")
            return None

    def get_next_earnings_date(self, ticker):
        try:
            return si.get_next_earnings_date(ticker)
        except Exception as e:
            print(f"Error fetching next earnings date: {e}")
            return None

    def get_premarket_price(self, ticker):
        try:
            return si.get_premarket_price(ticker)
        except Exception as e:
            print(f"Error fetching premarket price: {e}")
            return None

    def get_postmarket_price(self, ticker):
        try:
            return si.get_postmarket_price(ticker)
        except Exception as e:
            print(f"Error fetching postmarket price: {e}")
            return None

    def get_quote_data(self, ticker):
        try:
            return si.get_quote_data(ticker)
        except Exception as e:
            print(f"Error fetching quote data: {e}")
            return None

    def get_quote_table(self, ticker):
        try:
            return si.get_quote_table(ticker)
        except Exception as e:
            print(f"Error fetching quote table: {e}")
            return None

    def get_top_crypto(self):
        try:
            return si.get_top_crypto()
        except Exception as e:
            print(f"Error fetching top crypto: {e}")
            return None

    def get_splits(self, ticker):
        try:
            return si.get_splits(ticker)
        except Exception as e:
            print(f"Error fetching splits: {e}")
            return None

    def get_stats(self, ticker):
        try:
            return si.get_stats(ticker)
        except Exception as e:
            print(f"Error fetching stats: {e}")
            return None

    def get_stats_valuation(self, ticker):
        try:
            return si.get_stats_valuation(ticker)
        except Exception as e:
            print(f"Error fetching stats valuation: {e}")
            return None

    def get_undervalued_large_caps(self):
        try:
            return si.get_undervalued_large_caps()
        except Exception as e:
            print(f"Error fetching undervalued large caps: {e}")
            return None

    def tickers_dow(self):
        try:
            return si.tickers_dow()
        except Exception as e:
            print(f"Error fetching tickers dow: {e}")
            return None

    def tickers_ftse100(self):
        try:
            return si.tickers_ftse100()
        except Exception as e:
            print(f"Error fetching tickers ftse100: {e}")
            return None

    def tickers_ftse250(self):
        try:
            return si.tickers_ftse250()
        except Exception as e:
            print(f"Error fetching tickers ftse250: {e}")
            return None

    def tickers_ibovespa(self):
        try:
            return si.tickers_ibovespa()
        except Exception as e:
            print(f"Error fetching tickers ibovespa: {e}")
            return None

    def tickers_nasdaq(self):
        try:
            return si.tickers_nasdaq()
        except Exception as e:
            print(f"Error fetching tickers nasdaq: {e}")
            return None

    def tickers_nifty50(self):
        try:
            return si.tickers_nifty50()
        except Exception as e:
            print(f"Error fetching tickers nifty50: {e}")
            return None

    def tickers_niftybank(self):
        try:
            return si.tickers_niftybank()
        except Exception as e:
            print(f"Error fetching tickers niftybank: {e}")
            return None

    def tickers_other(self):
        try:
            return si.tickers_other()
        except Exception as e:
            print(f"Error fetching tickers other: {e}")
            return None

    def tickers_sp500(self):
        try:
            return si.tickers_sp500()
        except Exception as e:
            print(f"Error fetching tickers sp500: {e}")
            return None

    def get_calls(self, ticker, date=None):
        try:
            return options.get_calls(ticker, date)
        except Exception as e:
            print(f"Error fetching calls: {e}")
            return None

    def get_expiration_dates(self, ticker):
        try:
            return options.get_expiration_dates(ticker)
        except Exception as e:
            print(f"Error fetching expiration dates: {e}")
            return None

    def get_options_chain(self, ticker, date=None):
        try:
            return options.get_options_chain(ticker, date)
        except Exception as e:
            print(f"Error fetching options chain: {e}")
            return None

    def get_puts(self, ticker, date=None):
        try:
            return options.get_puts(ticker, date)
        except Exception as e:
            print(f"Error fetching puts: {e}")
            return None

    # YFinance Service
    def get_historical_data(self, ticker, period="1mo"):
        try:
            return self.yfinance_service.get_historical_data(ticker, period)
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return None

    def get_financials(self, ticker):
        try:
            return self.yfinance_service.get_financials(ticker)
        except Exception as e:
            print(f"Error fetching financials: {e}")
            return None

    def get_actions(self, ticker):
        try:
            return self.yfinance_service.get_actions(ticker)
        except Exception as e:
            print(f"Error fetching actions: {e}")
            return None

    def get_share_count(self, ticker, start="2022-01-01", end=None):
        try:
            return self.yfinance_service.get_share_count(ticker, start, end)
        except Exception as e:
            print(f"Error fetching share count: {e}")
            return None

    def get_holders(self, ticker):
        try:
            return self.yfinance_service.get_holders(ticker)
        except Exception as e:
            print(f"Error fetching holders: {e}")
            return None

    def get_recommendations(self, ticker):
        try:
            return self.yfinance_service.get_recommendations(ticker)
        except Exception as e:
            print(f"Error fetching recommendations: {e}")
            return None

    def get_earnings_dates(self, ticker):
        try:
            return self.yfinance_service.get_earnings_dates(ticker)
        except Exception as e:
            print(f"Error fetching earnings dates: {e}")
            return None

    def get_isin(self, ticker):
        try:
            return self.yfinance_service.get_isin(ticker)
        except Exception as e:
            print(f"Error fetching ISIN: {e}")
            return None

    def get_options(self, ticker):
        try:
            return self.yfinance_service.get_options(ticker)
        except Exception as e:
            print(f"Error fetching options: {e}")
            return None

    def get_news(self, ticker):
        try:
            return self.yfinance_service.get_news(ticker)
        except Exception as e:
            print(f"Error fetching news: {e}")
            return None

     # Alpha Vantage methods
    def get_alpha_vantage_intraday(self, ticker, interval='1min'):
        try:
            return self.alpha_vantage_service.get_intraday(ticker, interval)
        except Exception as e:
            print(f"Error fetching intraday data: {e}")
            return None

    def get_alpha_vantage_daily(self, ticker):
        try:
            return self.alpha_vantage_service.get_daily(ticker)
        except Exception as e:
            print(f"Error fetching daily data: {e}")
            return None

    def get_alpha_vantage_daily_adjusted(self, ticker):
        try:
            return self.alpha_vantage_service.get_daily_adjusted(ticker)
        except Exception as e:
            print(f"Error fetching daily adjusted data: {e}")
            return None

    def get_alpha_vantage_weekly(self, ticker):
        try:
            return self.alpha_vantage_service.get_weekly(ticker)
        except Exception as e:
            print(f"Error fetching weekly data: {e}")
            return None

    def get_alpha_vantage_weekly_adjusted(self, ticker):
        try:
            return self.alpha_vantage_service.get_weekly_adjusted(ticker)
        except Exception as e:
            print(f"Error fetching weekly adjusted data: {e}")
            return None

    def get_alpha_vantage_monthly(self, ticker):
        try:
            return self.alpha_vantage_service.get_monthly(ticker)
        except Exception as e:
            print(f"Error fetching monthly data: {e}")
            return None

    def get_alpha_vantage_monthly_adjusted(self, ticker):
        try:
            return self.alpha_vantage_service.get_monthly_adjusted(ticker)
        except Exception as e:
            print(f"Error fetching monthly adjusted data: {e}")
            return None

    def get_alpha_vantage_company_overview(self, ticker):
        try:
            return self.alpha_vantage_service.get_company_overview(ticker)
        except Exception as e:
            print(f"Error fetching company overview: {e}")
            return None

    def get_alpha_vantage_income_statement(self, ticker):
        try:
            return self.alpha_vantage_service.get_income_statement(ticker)
        except Exception as e:
            print(f"Error fetching income statement: {e}")
            return None

    def get_alpha_vantage_balance_sheet(self, ticker):
        try:
            return self.alpha_vantage_service.get_balance_sheet(ticker)
        except Exception as e:
            print(f"Error fetching balance sheet: {e}")
            return None

    def get_alpha_vantage_cash_flow(self, ticker):
        try:
            return self.alpha_vantage_service.get_cash_flow(ticker)
        except Exception as e:
            print(f"Error fetching cash flow: {e}")
            return None

    def get_alpha_vantage_sma(self, ticker, interval='daily', time_period=20, series_type='close'):
        try:
            return self.alpha_vantage_service.get_sma(ticker, interval, time_period, series_type)
        except Exception as e:
            print(f"Error fetching SMA: {e}")
            return None

    def get_alpha_vantage_ema(self, ticker, interval='daily', time_period=20, series_type='close'):
        try:
            return self.alpha_vantage_service.get_ema(ticker, interval, time_period, series_type)
        except Exception as e:
            print(f"Error fetching EMA: {e}")
            return None

    def get_alpha_vantage_macd(self, ticker, interval='daily', series_type='close'):
        try:
            return self.alpha_vantage_service.get_macd(ticker, interval, series_type)
        except Exception as e:
            print(f"Error fetching MACD: {e}")
            return None

    def get_alpha_vantage_rsi(self, ticker, interval='daily', time_period=14, series_type='close'):
        try:
            return self.alpha_vantage_service.get_rsi(ticker, interval, time_period, series_type)
        except Exception as e:
            print(f"Error fetching RSI: {e}")
            return None

    def get_alpha_vantage_sector(self):
        try:
            return self.alpha_vantage_service.get_sector()
        except Exception as e:
            print(f"Error fetching sector performance: {e}")
            return None

    def get_alpha_vantage_crypto_daily(self, symbol, market='USD'):
        try:
            return self.alpha_vantage_service.get_crypto_daily(symbol, market)
        except Exception as e:
            print(f"Error fetching cryptocurrency daily data: {e}")
            return None
