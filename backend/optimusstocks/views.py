from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Stock, Users, Portfolio, Question, Answer, Prediction, UnderstandingLevel
from .serializers import StockSerializer, UsersSerializer, PortfolioSerializer, QuestionSerializer, AnswerSerializer, PredictionSerializer, UnderstandingLevelSerializer
from .services.stock_service import StockService

# Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual Alpha Vantage API key
ALPHA_VANTAGE_API_KEY = settings.ALPHA_VANTAGE_API_KEY

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # Initialize the services
    stock_service = StockService(ALPHA_VANTAGE_API_KEY)

    # Custom action to fetch stock info
    @action(detail=True, methods=['get'])
    def stock_info(self, request, pk=None):
        ticker = self.get_object().ticker_symbol  # Assuming your Stock model has a ticker_symbol field
        
        stock_data = {
            # Yahoo Finance
            'quote_table': self.stock_service.get_yahoo_fin_info(ticker),
            'analysts_info': self.stock_service.get_analysts_info(ticker),
            'balance_sheet': self.stock_service.get_balance_sheet(ticker),
            'cash_flow': self.stock_service.get_cash_flow(ticker),
            'company_info': self.stock_service.get_company_info(ticker),
            'currencies': self.stock_service.get_currencies(),
            'data': self.stock_service.get_data(ticker),
            'day_gainers': self.stock_service.get_day_gainers(),
            'day_losers': self.stock_service.get_day_losers(),
            'day_most_active': self.stock_service.get_day_most_active(),
            'dividends': self.stock_service.get_dividends(ticker),
            'earnings': self.stock_service.get_earnings(ticker),
            'earnings_for_date': self.stock_service.get_earnings_for_date('YYYY-MM-DD'),
            'earnings_in_date_range': self.stock_service.get_earnings_in_date_range('YYYY-MM-DD', 'YYYY-MM-DD'),
            'earnings_history': self.stock_service.get_earnings_history(ticker),
            'financials': self.stock_service.get_financials(ticker),
            'futures': self.stock_service.get_futures(),
            'holders': self.stock_service.get_holders(ticker),
            'income_statement': self.stock_service.get_income_statement(ticker),
            'live_price': self.stock_service.get_live_price(ticker),
            'market_status': self.stock_service.get_market_status(),
            'next_earnings_date': self.stock_service.get_next_earnings_date(ticker),
            'premarket_price': self.stock_service.get_premarket_price(ticker),
            'postmarket_price': self.stock_service.get_postmarket_price(ticker),
            'quote_data': self.stock_service.get_quote_data(ticker),
            'top_crypto': self.stock_service.get_top_crypto(),
            'splits': self.stock_service.get_splits(ticker),
            'stats': self.stock_service.get_stats(ticker),
            'stats_valuation': self.stock_service.get_stats_valuation(ticker),
            'undervalued_large_caps': self.stock_service.get_undervalued_large_caps(),
            'tickers_dow': self.stock_service.tickers_dow(),
            'tickers_ftse100': self.stock_service.tickers_ftse100(),
            'tickers_ftse250': self.stock_service.tickers_ftse250(),
            'tickers_ibovespa': self.stock_service.tickers_ibovespa(),
            'tickers_nasdaq': self.stock_service.tickers_nasdaq(),
            'tickers_nifty50': self.stock_service.tickers_nifty50(),
            'tickers_niftybank': self.stock_service.tickers_niftybank(),
            'tickers_other': self.stock_service.tickers_other(),
            'tickers_sp500': self.stock_service.tickers_sp500(),
            'calls': self.stock_service.get_calls(ticker),
            'expiration_dates': self.stock_service.get_expiration_dates(ticker),
            'options_chain': self.stock_service.get_options_chain(ticker),
            'puts': self.stock_service.get_puts(ticker),
            'stock_news': self.stock_service.get_stock_news(ticker),

            # Alpha Vantage
            'alpha_vantage_intraday': self.stock_service.get_alpha_vantage_intraday(ticker),
            'alpha_vantage_daily': self.stock_service.get_alpha_vantage_daily(ticker),
            'alpha_vantage_daily_adjusted': self.stock_service.get_alpha_vantage_daily_adjusted(ticker),
            'alpha_vantage_weekly': self.stock_service.get_alpha_vantage_weekly(ticker),
            'alpha_vantage_weekly_adjusted': self.stock_service.get_alpha_vantage_weekly_adjusted(ticker),
            'alpha_vantage_monthly': self.stock_service.get_alpha_vantage_monthly(ticker),
            'alpha_vantage_monthly_adjusted': self.stock_service.get_alpha_vantage_monthly_adjusted(ticker),
            'alpha_vantage_company_overview': self.stock_service.get_alpha_vantage_company_overview(ticker),
            'alpha_vantage_income_statement': self.stock_service.get_alpha_vantage_income_statement(ticker),
            'alpha_vantage_balance_sheet': self.stock_service.get_alpha_vantage_balance_sheet(ticker),
            'alpha_vantage_cash_flow': self.stock_service.get_alpha_vantage_cash_flow(ticker),
            'alpha_vantage_sma': self.stock_service.get_alpha_vantage_sma(ticker),
            'alpha_vantage_ema': self.stock_service.get_alpha_vantage_ema(ticker),
            'alpha_vantage_macd': self.stock_service.get_alpha_vantage_macd(ticker),
            'alpha_vantage_rsi': self.stock_service.get_alpha_vantage_rsi(ticker),
            'alpha_vantage_sector': self.stock_service.get_alpha_vantage_sector(),
            'alpha_vantage_crypto_daily': self.stock_service.get_alpha_vantage_crypto_daily(ticker),

            # YFinance
            'yfinance_info': self.stock_service.get_yfinance_info(ticker),
            'historical_data': self.stock_service.get_historical_data(ticker),
            'actions': self.stock_service.get_actions(ticker),
            'share_count': self.stock_service.get_share_count(ticker),
            'financials_yf': self.stock_service.get_financials(ticker),
            'holders_yf': self.stock_service.get_holders(ticker),
            'recommendations': self.stock_service.get_recommendations(ticker),
            'earnings_dates': self.stock_service.get_earnings_dates(ticker),
            'isin': self.stock_service.get_isin(ticker),
            'options_yf': self.stock_service.get_options(ticker),
            'news_yf': self.stock_service.get_news(ticker),
            'option_chain': self.stock_service.get_option_chain(ticker, 'YYYY-MM-DD')
            
        }

        return Response(stock_data, status=status.HTTP_200_OK)                                      


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer


class UnderstandingLevelViewSet(viewsets.ModelViewSet):
    queryset = UnderstandingLevel.objects.all()
    serializer_class = UnderstandingLevelSerializer

    
