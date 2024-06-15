import requests
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fetch fundamental data for specified stock'

    FUNCTION_CHOICES = [
        'OVERVIEW', 
        'DIVIDENDS', 
        'SPLITS', 
        'INCOME_STATEMENT', 
        'BALANCE_SHEET', 
        'CASH_FLOW', 
        'EARNINGS', 
        'LISTING_STATUS', 
        'IPO_CALENDAR']
    
    def add_arguments(self, parser):
        parser.add_argument('function',type=str, choices=self.FUNCTION_CHOICES, help= 'Function of your choice')
        parser.add_argument('symbol', type=str, help= 'Stock symbol')
        parser.add_argument('--date', type=str, help= 'Date for which you want data')
        parser.add_argument('--state', type=str, choices= ['active', 'delisted'], help= 'State of the company (by default, state is active)')


    def handle(self, *args, **kwargs):
        function = kwargs['function']
        symbol = kwargs['symbol']
        date = kwargs.get('date')
        state = kwargs.get('state')
        api_key = settings.ALPHA_VANTAGE_API_KEY
        
        base_url = 'https://www.alphavantage.co/query?'
        params = {
            'function': function,
            'symbol': symbol,
            'apikey': api_key}

        if function == 'LISTING_STATUS':
            if date:
                params['date'] = date
            if state:
                params['state'] = state 

        api_key_param = params.pop('api_key')



        url = base_url + '&'.join([f'{key}={value}' for key, value in params.items()])
        url += f'&apikey={api_key_param}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        
            self.stdout.write(self.style.SUCCESS('Successfully fetched data'))
            self.stdout.write(self.style.SUCCESS(str(data)))
        
        except requests.exceptions.HTTPError as http_err:
            self.stdout.write(self.style.ERROR(f'HTTP error occurred: {http_err}'))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f'An error occurred: {err}'))
            