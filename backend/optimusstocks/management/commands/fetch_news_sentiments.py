import requests
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Fetch news and sentiments from news outlet'
    
    
    def add_arguments(self, parser):
        parser.add_argument('--tickers', type=str, default= 'AAPL', help= 'Comma-separated list of stock/crypto/forex symbols')
        parser.add_argument('--topics', type=str, help='Comma-separated list of news topics')
        parser.add_argument('--time_from', type=str, help='Start time in YYYYMMDDTHHMM format')
        parser.add_argument('--time_to', type=str, help='End time in YYYYMMDDTHHMM format')
        parser.add_argument('--sort', type=str, default='LATEST', help='LATEST, EARLIEST, RELEVANCE')
        parser.add_argument('--limit', type=int, default=50, help='Number of results to return')
        
        
        
    def handle(self, *args, **kwargs):
        apikey = settings.ALPHA_VANTAGE_API_KEY
        tickers = kwargs['tickers']
        topics = kwargs['topics']
        time_from = kwargs['time_from']
        time_to = kwargs['time_to']
        sort = kwargs['sort']
        limit = kwargs['limit']
        
        url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey={apikey}'
        
        if tickers:
            url += f'&tickers={tickers}'
        if topics:
            url += f'&topics={topics}'
        if time_from:
            url += f'&time_from={time_from}'
        if time_to:
            url += f'&time_to={time_to}'
        if sort:
            url += f'&sort={sort}'
        if limit:
            url += f'&limit={limit}'
            
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()   
                 
            self.stdout.write(self.style.SUCCESS('Successfully fetched data'))   
            self.stdout.write(self.style.SUCCESS(str(data)))

        except requests.exceptions.HTTPError as http_err:
            self.stdout.write(self.style.ERROR('An error occured: {http_err}'))
        except Exception as err:
            self.stdout.write(self.style.ERROR('An error occured: {http_err}'))

            