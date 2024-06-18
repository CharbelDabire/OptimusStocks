import urllib
import requests
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Fetch news and sentiments from news outlet'

    TOPICS = [ 
              'blockchain'
              'earnings',
              'ipo',
              'mergers_and_acquisitions',
              'financial_markets',
              'economy_fiscal',
              'economy_monetary',
              'economy_macro',
              'energy_transportation',
              'finance',
              'life_sciences',
              'manufacturing',
              'real_estate',
              'retail_wholesale',
              'technology']
    
    
    def add_arguments(self, parser):
        parser.add_argument('--tickers', type=str, default= 'AAPL', help= 'Comma-separated list of stock symbols')
        parser.add_argument('--topics', type=str, choices= self.TOPICS, help='Comma-separated list of news topics')
        parser.add_argument('--time_from', type=str, help='Start time in YYYYMMDDTHHMM format')
        parser.add_argument('--time_to', type=str, help='End time in YYYYMMDDTHHMM format')
        parser.add_argument('--sort', type=str, default='LATEST', help='LATEST, EARLIEST, RELEVANCE')
        parser.add_argument('--limit', type=int, default=50, help='Number of results to return')
        
        
        
    def handle(self, *args, **kwargs):
        apikey = settings.ALPHA_VANTAGE_API_KEY
        tickers = kwargs.get('tickers')
        topics = kwargs.get('topics')
        time_from = kwargs.get('time_from')
        time_to = kwargs.get('time_to')
        sort = kwargs.get('sort')
        limit = kwargs.get('limit')
        
        url_base = 'https://www.alphavantage.co/query?'
        params = {'function': 'NEWS_SENTIMENT'}
        
        if tickers:
            params['tickers'] = tickers
        if topics:
            params['topics'] = topics
        if time_from:
            params['time_from'] = time_from
        if time_to:
            params['time_to'] = time_to    
        if sort:
            params['sort'] = sort
        if limit:
            params['limit'] = limit

        
        url = url_base + urllib.parse.urlencode(params)
        url += f'&apikey={apikey}'
            
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()   
                 
            self.stdout.write(self.style.SUCCESS('Successfully fetched data'))   
            self.stdout.write(self.style.SUCCESS(str(data)))

        except requests.exceptions.HTTPError as http_err:
            self.stdout.write(self.style.ERROR('An error occurred: {http_err}'))
        except Exception as err:
            self.stdout.write(self.style.ERROR('An error occurred: {http_err}'))

            