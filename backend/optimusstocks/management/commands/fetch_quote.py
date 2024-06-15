import requests
from django.core.management.base import BaseCommand
from optimusstocks.models import Stock
from django.conf import settings
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch latest price and volume information for a given ticker'
    
    def add_arguments(self, parser):
        parser.add_argument('symbol', type=str, help='Stock symbol')
        
        def handle(self, *args, **kwargs):
            symbol = kwargs['symbol']
            api_key = settings.ALPHA_VANTAGE_API_KEY
            
            
            url = f'httos://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
            response = requests.get(url)
            data = response.json()
            
            
            if 'Global Quote' in data:
                quote = data['Global Quote']
                stock, created = Stock.objects.update_or_create(
                    symbol=symbol,
                    defaults={
                        'open': quote['02. open'],
                        'high': quote['03. high'],
                        'low': quote['04. low'],
                        'price': quote['05. price'],
                        'volume': quote['06. volume'],
                        'latest_trading_day': datetime.strptime(quote['07. latest trading day'], '%Y-%m-%d'),
                        'previous_close': quote['08. previous close'],
                        'change': quote['09. change'],
                        'change_percentage': quote['10. change percent']                        
                    }
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully fetched quote for {symbol}'))
            else:
                self.stdout.write(self.style.ERROR('Error fetching data'))
            
      