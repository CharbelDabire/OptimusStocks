from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Stock, Users, Portfolio, Question, Answer, Prediction, UnderstandingLevel
from .serializers import StockSerializer, UsersSerializer, PortfolioSerializer, QuestionSerializer, AnswerSerializer, PredictionSerializer, UnderstandingLevelSerializer
from .services.stock_service import StockService
from .services.alpha_vantage_service import AlphaVantageService
from .services.yahoo_fin_service import YahooFinService
from .services.yfinance_service import YFinanceService

# Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual Alpha Vantage API key
ALPHA_VANTAGE_API_KEY = settings.ALPHA_VANTAGE_API_KEY

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # Initialize the services
    stock_service = StockService(ALPHA_VANTAGE_API_KEY)
    yahoo_fin_service = YahooFinService()
    yfinance_service = YFinanceService()

    # Custom action to fetch stock info
    @action(detail=True, methods=['get'])
    def stock_info(self, request, pk=None):
        ticker = self.get_object().ticker_symbol  # Assuming your Stock model has a ticker_symbol field
        stock_info = self.stock_service.get_stock_info(ticker)
        stock_news = self.stock_service.get_stock_news(ticker)
        stock_options = self.stock_service.get_stock_options(ticker)

        return Response({
            'stock_info': stock_info,
            'stock_news': stock_news,
            'stock_options': stock_options
        }, status=status.HTTP_200_OK)


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

    
