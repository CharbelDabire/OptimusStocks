import yfinance as yf

class YFinanceService:
    def get_stock_info(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.info

    def get_historical_data(self, ticker, period="1mo"):
        stock = yf.Ticker(ticker)
        return stock.history(period=period)

    def get_history_metadata(self, ticker):
        stock = yf.Ticker(ticker)
        stock.history(period="1mo")  # Ensure history is called first
        return stock.history_metadata

    def get_actions(self, ticker):
        stock = yf.Ticker(ticker)
        return {
            "actions": stock.actions,
            "dividends": stock.dividends,
            "splits": stock.splits,
            "capital_gains": stock.capital_gains
        }

    def get_share_count(self, ticker, start="2022-01-01", end=None):
        stock = yf.Ticker(ticker)
        return stock.get_shares_full(start=start, end=end)

    def get_financials(self, ticker):
        stock = yf.Ticker(ticker)
        return {
            "income_stmt": stock.income_stmt,
            "quarterly_income_stmt": stock.quarterly_income_stmt,
            "balance_sheet": stock.balance_sheet,
            "quarterly_balance_sheet": stock.quarterly_balance_sheet,
            "cashflow": stock.cashflow,
            "quarterly_cashflow": stock.quarterly_cashflow
        }

    def get_holders(self, ticker):
        stock = yf.Ticker(ticker)
        return {
            "major_holders": stock.major_holders,
            "institutional_holders": stock.institutional_holders,
            "mutualfund_holders": stock.mutualfund_holders,
            "insider_transactions": stock.insider_transactions,
            "insider_purchases": stock.insider_purchases,
            "insider_roster_holders": stock.insider_roster_holders
        }

    def get_recommendations(self, ticker):
        stock = yf.Ticker(ticker)
        return {
            "recommendations": stock.recommendations,
            "recommendations_summary": stock.recommendations_summary,
            "upgrades_downgrades": stock.upgrades_downgrades
        }

    def get_earnings_dates(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.earnings_dates

    def get_isin(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.isin

    def get_options(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.options

    def get_news(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.news

    def get_option_chain(self, ticker, date):
        stock = yf.Ticker(ticker)
        opt = stock.option_chain(date)
        return {
            "calls": opt.calls,
            "puts": opt.puts
        }
