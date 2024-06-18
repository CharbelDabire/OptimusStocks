import requests
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Search for symbols based on keywords'
    
    def add_arguments(self, parser):
        parser.add_argument('keywords', type=str, help='Search keywords')
        
    def handle(self, *args, **kwargs):
            keywords = kwargs['keywords']
            api_key = settings.ALPHA_VANTAGE_API_KEY
            
            url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={api_key}'    
    
            try:
                r = requests.get(url)
                r.raise_for_status() 
                data = r.json()

                if "bestMatches" in data:
                    for match in data["bestMatches"]:
                        print(f"Symbol: {match['1. symbol']}, Name: {match['2. name']}")
                    else:
                        self.stdout.write(self.style.WARNING('No matches found.'))
                else:
                    self.stdout.write(self.style.ERROR(f'Error fetching data'))     
                

            except requests.exceptions.RequestException as e:
                self.stderr.write(self.style.ERROR(f'Error fetching data'))

        
    