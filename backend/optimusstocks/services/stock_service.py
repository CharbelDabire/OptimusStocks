import logging
from backend.optimusstocks.services.alpha_vantage_service import AlphaVantageService
from backend.optimusstocks.services.yahoo_fin_service import YahooFinService
from backend.optimusstocks.services.yfinance_service import YFinanceService

class StockService:
    def __init__(self, alpha_vantage_api_key, yahoo_fin_service=None, yfinance_service=None, alpha_vantage_service=None):
        self.alpha_vantage_service = alpha_vantage_service or AlphaVantageService(alpha_vantage_api_key)
        self.yfinance_service = yfinance_service or YFinanceService()
        self.yahoo_fin_service = yahoo_fin_service or YahooFinService()

    def __getattr__(self, name):
        def method(*args , **kwargs):
            for service in [self.alpha_vantage_service, self.yfinance_service, self.yahoo_fin_service]:
                if hasattr(service, name):
                    try:
                        return getattr(service, name)(*args, **kwargs)
                    except Exception as e:
                        self.logger.error(f"Error calling {name}: {e}")
                        return None
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        return method

    