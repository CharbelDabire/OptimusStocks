from typing import Any
import requests
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Fetch the 20 top gainers and loosers and most active traded tickers in US market'

    def add_arguments(self, parser):
        parser.add_argument('apikeyd')
    
           
    def handle(self, *args, **kwargs):
        apikey = settings.ALPHA_VANTAGE_API_KEY
        
        url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOOSERS$apikey={apikey}'
        
        try:

            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
        
            # Print or process the data as needed
            self.stdout.write(self.style.SUCCESS('Successfully  fetched data:'))
            self.stdout.write(self.style.SUCCESS(str(data)))

        except requests.exceptions.HTTPError as http_err:
            self.stdout.write(self.style.ERROR(f'HTTP error occured: {http_err}'))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f'An error occured: {err}'))

            

            

        