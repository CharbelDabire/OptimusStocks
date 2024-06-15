import requests
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fetch key US economic indicators for investing strategies'

    FUNCTION_CHOICES = [
        'REAL_GDP',
        'REAL_GDP_PER_CAPITA',
        'TREASURY_YIELD',
        'FEDERAL_FUNDS_RATE',
        'CPI',
        'INFLATION', 
        'RETAIL_SALES',
        'DURABLES', 
        'UNEMPLOYMENT',
        'NONFARM_PAYROLL']

    def add_arguments(self, parser):
        parser.add_argument('function', type=str, choices= self.FUNCTION_CHOICES, help='Function of your choice (e.g. REAL_GDP, REAL_GDP_PER_CAPITA, UNEMPLOYMENT)')
        parser.add_argument('--interval', type=str, choices=['quarterly', 'annual'], default='annual', help='Interval of your choice (annual by default)')
        parser.add_argument('--datatype', type=str, choices=['json', 'csv'], default='json', help=' data type of your choice (json by default)')
        parser.add_argument('--maturity', type=str, choices=['3month', '2year','5year', ' 7year', '10year', '30year'], default='10year', help= ' maturity timeline for yield on U.S. Treasury Securities')


    def handle(self, *args, **kwargs):
        function = kwargs['function']
        interval = kwargs.get('interval')
        datatype = kwargs.get('datatype')
        maturity = kwargs.get('maturity')
        api_key = settings.ALPHA_VANTAGE_API_KEY

        url_base = 'https://www.alphavantage.co/query?'

        params = {
            'function': function,
            }

        if interval and function in {'REAL_GDP', 'TREASURY_YIELD', 'FEDERAL_FUNDS_RATE', 'CPI'}:
            params['interval'] = interval
        if datatype:
            params['datatype'] = datatype
        if maturity and function == 'TREASURY_YIELD':
            params['maturity'] = maturity

        url = url_base + '&'.join([f'{k}={v}' for k, v in params.items()])
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

    