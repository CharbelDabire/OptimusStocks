import requests
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fetch analytics on specified stocks'

    def add_arguments(self, parser):
        
        parser.add_argument('symbols', type=str, help='A comma separated list of symbols')
        parser.add_argument('range', type=str, help='Date range for the series (e.g., full, {N}day, {N}week, 2023-07-01, YYYY-MM, etc )')
        parser.add_argument('interval', type=str, choices=['1min', '5min', '15min', '30min', '60min', 'DAILY', 'WEEKLY', 'MONTHLY'], help='Time interval between data points')
        parser.add_argument('calculations', type=str, help='A comma separated list of the analytics metrics to calculate')
        parser.add_argument('--ohlc', type=str, choices=['open', 'high', 'low', 'close'], default='close', help='The field (open, high, low, or close) on which the calculations will be performed')

        # parser.add_argument('apikey', type=str, help='API key for Alpha Vantage')
        # choices=['full, {N}day, {N}week, {N}month, {N}year, {N}minute, {N}hour'],
        # choices=[]
       
    def handle(self, *args, **kwargs):
        apikey = settings.ALPHA_VANTAGE_API_KEY
        symbols = kwargs['symbols']
        range = kwargs['range']
        interval = kwargs['interval']
        calculations = kwargs['calculations']
        ohlc = kwargs['ohlc']


        calculations_list = calculations.split(',')

        valid_basic_calculations = {'MIN', 'MAX', 'MEAN', 'MEDIAN', 'STDDEV', 'CUMULATIVE_RETURN', 'VARIANCE', 'MAX_DRAWDOWN', 'HISTOGRAM', 'AUTOCORRELATION', 'COVARIANCE', 'CORRELATION'}
        valid_complex_calculations = {'VARIANCE(annualized=True)', 'STDDEV(annualized=True)',  'HISTOGRAM(bins={N})',  'COVARIANCE(annualized=True)', 'AUTOCORRELATION(lag={N})', 'CORRELATION(method=KENDALL)', 'CORRELATION(method=SPEARMAN)'}

        for calc in calculations_list:
            calc = calc.strip()
            if calc in valid_basic_calculations:
                continue
            elif any(calc.startswith(valid_complex_calculations) for valid_complex in valid_complex_calculations):
                continue
            else:
                self.stdout.write(self.style.ERROR(f'Invalid calculation: {calc}'))
            

        

        url_base = 'https://www.alphavantage.co/query?function=ANALYTICS_FIXED_WINDOW&'
        params = {
            'SYMBOLS': symbols,
            'RANGE': range,
            'INTERVAL': interval,
            'CALCULATIONS': calculations}

        if ohlc:
            params['OHLC'] = ohlc


        url = url_base + urllib.parse.urlencode(params)
        url += f'&apikey={apikey}'
        
            

        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()

            self.stdout.write(self.style.SUCCESS('Successfully fetched data'))
            self.stdout.write(self.style.SUCCESS(str(data)))

        except requests.exceptions.HTTPError as http_err:
            self.stdout.write(self.style.ERROR(f'HTTP error occurred: {http_err}'))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f'An error occurred: {err}'))
            