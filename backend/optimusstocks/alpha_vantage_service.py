# stocks/services/stock_service.py
from .alpha_vantage_service.py import AlphaVantageService
from .yahoo_fin_service.py import YahooFinService
from .yfinance_service.py import YFinanceService

class StockService:
    def __init__(self, alpha_vantage_api_key):
        self.alpha_vantage_service = AlphaVantageService(alpha_vantage_api_key)
        self.yahoo_fin_service = YahooFinService()
        self.yfinance_service = YFinanceService()

    def get_stock_info(self, ticker):
        try:
            return self.yahoo_fin_service.get_stock_info(ticker)
        except Exception as e1:
            print(f"Error with Yahoo Finance: {e1}")
            try:
                return self.yfinance_service.get_stock_info(ticker)
            except Exception as e2:
                print(f"Error with yfinance: {e2}")
                return self.alpha_vantage_service.get_stock_info(ticker)

    def get_stock_news(self, ticker):
        return self.yahoo_fin_service.get_stock_news(ticker)

    def get_stock_options(self, ticker):
        return self.yahoo_fin_service.get_stock_options(ticker)

    def get_fundamental_data(self, ticker):
        return self.alpha_vantage_service.get_fundamental_data(ticker)

    def get_technical_indicators(self, ticker, indicator):
        return self.alpha_vantage_service.get_technical_indicators(ticker, indicator)

    def get_sector_performance(self):
        return self.alpha_vantage_service.get_sector_performance()

    def get_crypto_data(self, symbol):
        return self.alpha_vantage_service.get_crypto_data(symbol)
