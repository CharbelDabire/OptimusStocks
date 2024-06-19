import urllib.parse
import requests
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help= 'Fetch market status of major trading venues'

    def add_arguments(self, parser):
        parser.add_argument('function', type=str, help='MARKET_STATUS')
        parser.add_argument('apikey', type=str, help='API key')

    def handle(self, *args, **kwargs):
        function = kwargs['function'] = 'MARKET_STATUS'
        apikey = settings.ALPHA_VANTAGE_API_KEY

        url_base = 'https://www.alphavantage.co/query?'
        params = {
            'function': function,
            'apikey': apikey
            }

        url = url_base + urllib.parse.urlencode(params)

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
        