from rest_framework import viewsets
from .models import Stock, User, Portfolio, Question, Answer, Prediction, UnderstandingLevel
from .serializers import StockSerializer, UserSerializer, PortfolioSerializer, QuestionSerializer, AnswerSerializer, PredictionSerializer, UnderstandingLevelSerializer

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

    
