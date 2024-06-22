from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    open = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    high = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    low = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    close = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volume = models.BigIntegerField(null=True, blank=True)
    latest_trading_day = models.DateField(null=True, blank=True)
    previous_close = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    change = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    change_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.symbol} - {self.price}"

class StockInfo(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    


class HistoricalData(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.stock.symbol} - {self.date}"


class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Users, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Portfolio(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    stocks = models.ManyToManyField(Stock)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s portfolio"


class Question(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) :
        return self.text
    
class Prediction(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    predicted_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Prediction for {self.stock.symbol}"
    
class UnderstandingLevel(models.Model):
        user = models.ForeignKey(Users, on_delete=models.CASCADE)
        level = models.IntegerField()

        def __str__(self):
            return f"{self.user.username}'s understanding level"




