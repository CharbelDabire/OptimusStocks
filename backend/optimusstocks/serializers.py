from rest_framework import serializers
from .models import Stock, User, Portfolio, Question, Answer, Prediction, UnderstandingLevel 

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class PortfolioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    stocks = StockSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'



class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'


class PredictionSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)

    class Meta:
        model = Prediction
        fields = '__all__'


class UnderstandingLevelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UnderstandingLevel
        fields = '__all__'


