from rest_framework import serializers
from .models import Stock, Users, Portfolio, Question, Answer, Prediction, UnderstandingLevel 

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'password']


class PortfolioSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)
    stocks = StockSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)

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
    user = UsersSerializer(read_only=True)
    
    class Meta:
        model = UnderstandingLevel
        fields = '__all__'


