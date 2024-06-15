import requests
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fetch list of expected company earnings in the next 3 to 12 months'

    def add_arguments(self, parser):
        parser.add_argument('--symbol', type=str, default=None, help='tickers for which you want list of earnings schedule')
        parser.add_argument('--horizon', type=str, choices=['3month', '6month', '12month'], default='3month', help='Earning schedules for the next defined horizon') 


    def handle(self, *args, **kwargs):
        symbol = kwargs.get('symbol')
        horizon = kwargs.get('horizon', '3month')
        api_key = settings.ALPHA_VANTAGE_API_KEY
        
        url_base = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR'
        params = {
            horizon: horizon}
        if symbol:
            params['symbol'] = symbol

        url = url_base + '&'.join([f'{key}={value}' for key, value in params.items()])
        url += f'&apikey={api_key}'

        
        
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

        
        