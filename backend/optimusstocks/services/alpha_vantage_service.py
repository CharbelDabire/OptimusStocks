from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies

class AlphaVantageService:
    def __init__(self, api_key):
        self.ts = TimeSeries(key=api_key)
        self.fd = FundamentalData(key=api_key)
        self.ti = TechIndicators(key=api_key)
        self.sp = SectorPerformances(key=api_key)
        self.cc = CryptoCurrencies(key=api_key)

    # Time Series data
    def get_intraday(self, symbol, interval='1min'):
        try:
            data, _ = self.ts.get_intraday(symbol=symbol, interval=interval)
            return data
        except Exception as e:
            print(f"Error fetching intraday data: {e}")
            return None

    def get_daily(self, symbol):
        try:
            data, _ = self.ts.get_daily(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching daily data: {e}")
            return None

    def get_daily_adjusted(self, symbol):
        try:
            data, _ = self.ts.get_daily_adjusted(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching daily adjusted data: {e}")
            return None

    def get_weekly(self, symbol):
        try:
            data, _ = self.ts.get_weekly(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching weekly data: {e}")
            return None

    def get_weekly_adjusted(self, symbol):
        try:
            data, _ = self.ts.get_weekly_adjusted(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching weekly adjusted data: {e}")
            return None

    def get_monthly(self, symbol):
        try:
            data, _ = self.ts.get_monthly(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching monthly data: {e}")
            return None

    def get_monthly_adjusted(self, symbol):
        try:
            data, _ = self.ts.get_monthly_adjusted(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching monthly adjusted data: {e}")
            return None

    # Fundamental Data
    def get_company_overview(self, symbol):
        try:
            data, _ = self.fd.get_company_overview(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching company overview: {e}")
            return None

    def get_income_statement(self, symbol):
        try:
            data, _ = self.fd.get_income_statement(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching income statement: {e}")
            return None

    def get_balance_sheet(self, symbol):
        try:
            data, _ = self.fd.get_balance_sheet(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching balance sheet: {e}")
            return None

    def get_cash_flow(self, symbol):
        try:
            data, _ = self.fd.get_cash_flow(symbol=symbol)
            return data
        except Exception as e:
            print(f"Error fetching cash flow: {e}")
            return None

    # Technical Indicators
    def get_sma(self, symbol, interval='daily', time_period=20, series_type='close'):
        try:
            data, _ = self.ti.get_sma(symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)
            return data
        except Exception as e:
            print(f"Error fetching SMA: {e}")
            return None

    def get_ema(self, symbol, interval='daily', time_period=20, series_type='close'):
        try:
            data, _ = self.ti.get_ema(symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)
            return data
        except Exception as e:
            print(f"Error fetching EMA: {e}")
            return None

    def get_macd(self, symbol, interval='daily', series_type='close'):
        try:
            data, _ = self.ti.get_macd(symbol=symbol, interval=interval, series_type=series_type)
            return data
        except Exception as e:
            print(f"Error fetching MACD: {e}")
            return None

    def get_rsi(self, symbol, interval='daily', time_period=14, series_type='close'):
        try:
            data, _ = self.ti.get_rsi(symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)
            return data
        except Exception as e:
            print(f"Error fetching RSI: {e}")
            return None

    # Sector Performances
    def get_sector(self):
        try:
            data, _ = self.sp.get_sector()
            return data
        except Exception as e:
            print(f"Error fetching sector performance: {e}")
            return None

    # Cryptocurrencies
    def get_crypto_daily(self, symbol, market='USD'):
        try:
            data, _ = self.cc.get_digital_currency_daily(symbol=symbol, market=market)
            return data
        except Exception as e:
            print(f"Error fetching crypto daily data: {e}")
            return None
