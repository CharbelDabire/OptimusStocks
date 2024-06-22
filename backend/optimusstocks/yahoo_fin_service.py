from yahoo_fin import stock_info as si
from yahoo_fin import options
from yahoo_fin import news

class YahooFinService:
    def get_analysts_info(self, ticker):
        return si.get_analysts_info(ticker)
    
    def get_balance_sheet(self, ticker):
        return si.get_balance_sheet(ticker)
    
    def get_cash_flow(self, ticker):
        return si.get_cash_flow(ticker)
    
    def get_company_info(self, ticker):
        return si.get_company_info(ticker)
    
    def get_currencies(self):
        return si.get_currencies()
    
    def get_data(self, ticker, start_date=None, end_date=None, index_as_date=True):
        return si.get_data(ticker, start_date=start_date, end_date=end_date, index_as_date=index_as_date)
    
    def get_day_gainers(self):
        return si.get_day_gainers()
    
    def get_day_losers(self):
        return si.get_day_losers()
    
    def get_day_most_active(self):
        return si.get_day_most_active()
    
    def get_dividends(self, ticker):
        return si.get_dividends(ticker)
    
    def get_earnings(self, ticker):
        return si.get_earnings(ticker)
    
    def get_earnings_for_date(self, date):
        return si.get_earnings_for_date(date)
    
    def get_earnings_in_date_range(self, start_date, end_date):
        return si.get_earnings_in_date_range(start_date, end_date)
    
    def get_earnings_history(self, ticker):
        return si.get_earnings_history(ticker)
    
    def get_financials(self, ticker):
        return si.get_financials(ticker)
    
    def get_futures(self):
        return si.get_futures()
    
    def get_holders(self, ticker):
        return si.get_holders(ticker)
    
    def get_income_statement(self, ticker):
        return si.get_income_statement(ticker)
    
    def get_live_price(self, ticker):
        return si.get_live_price(ticker)
    
    def get_market_status(self):
        return si.get_market_status()
    
    def get_next_earnings_date(self, ticker):
        return si.get_next_earnings_date(ticker)
    
    def get_premarket_price(self, ticker):
        return si.get_premarket_price(ticker)
    
    def get_postmarket_price(self, ticker):
        return si.get_postmarket_price(ticker)
    
    def get_quote_data(self, ticker):
        return si.get_quote_data(ticker)
    
    def get_quote_table(self, ticker):
        return si.get_quote_table(ticker)
    
    def get_top_crypto(self):
        return si.get_top_crypto()
    
    def get_splits(self, ticker):
        return si.get_splits(ticker)
    
    def get_stats(self, ticker):
        return si.get_stats(ticker)
    
    def get_stats_valuation(self, ticker):
        return si.get_stats_valuation(ticker)
    
    def get_undervalued_large_caps(self):
        return si.get_undervalued_large_caps()
    
    def tickers_dow(self):
        return si.tickers_dow()
    
    def tickers_ftse100(self):
        return si.tickers_ftse100()
    
    def tickers_ftse250(self):
        return si.tickers_ftse250()
    
    def tickers_ibovespa(self):
        return si.tickers_ibovespa()
    
    def tickers_nasdaq(self):
        return si.tickers_nasdaq()
    
    def tickers_nifty50(self):
        return si.tickers_nifty50()
    
    def tickers_niftybank(self):
        return si.tickers_niftybank()
    
    def tickers_other(self):
        return si.tickers_other()
    
    def tickers_sp500(self):
        return si.tickers_sp500()
    
    def get_calls(self, ticker, date=None):
        return options.get_calls(ticker, date)
    
    def get_expiration_dates(self, ticker):
        return options.get_expiration_dates(ticker)
    
    def get_options_chain(self, ticker, date=None):
        return options.get_options_chain(ticker, date)
    
    def get_puts(self, ticker, date=None):
        return options.get_puts(ticker, date)
    
    def get_stock_news(self, ticker):
        return news.get_yf_rss(ticker)
