# stocks/services/yfinance_service.py
import yfinance as yf

class YFinanceService:
    def get_stock_info(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.info
