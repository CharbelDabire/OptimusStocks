# stocks/services/yahoo_fin_service.py
from yahoo_fin import stock_info as si
from yahoo_fin import options
from yahoo_fin import news

class YahooFinService:
    def get_stock_info(self, ticker):
        return si.get_quote_table(ticker)

    def get_stock_news(self, ticker):
        return news.get_yf_rss(ticker)

    def get_stock_options(self, ticker):
        return options.get_options_chain(ticker)
