import requests
from django.conf import settings
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Fetch analytics for list of stocks over sliding time windows'

    def add_arguments(self, parser):
        parser.add_argument('symbols', type=str, help='A comma separated list of symbols')
        parser.add_argument('range', type=str, help='Date range for the series (e.g., full, {N}day, {N}week, 2023-07-0)')
        parser.add_argument('interval', type=str, help='Time interval between data points')
        parser.add_argument('window', type=str, help='Sliding window size')
        parser.add_argument('calculations', type=str, help='A comma separated list of the analytics metrics to calculate')


    def handle(self, *args, **kwargs):
        symbols = kwargs['symbols']
        range = kwargs['range']
        interval = kwargs['interval']
        window = kwargs['window']
        calculations = kwargs['calculations']
        apikey = settings.ALPHA_VANTAGE_API_KEY


        calculations_list = calculations.split(',')

        valid_basic_calculations = {'MEAN', 'MEDIAN', 'STDDEV', 'CUMULATIVE_RETURN', 'VARIANCE', 'COVARIANCE', 'CORRELATION'}
        valid_complex_calculations = {'VARIANCE(annualized=True)', 'STDDEV(annualized=True)',  'COVARIANCE(annualized=True)', 'CORRELATION(method=KENDALL)', 'CORRELATION(method=SPEARMAN)'}

        
        for calc in calculations_list:
            calc = calc.strip()
            if calc in valid_basic_calculations:
                continue
            elif calc in valid_complex_calculations:
                if any(calc.startswith(valid_complex_calculations for valid_complex in valid_complex_calculations)):
                    continue
            else:
                self.stadout.write(self.style.ERROR(f'Invalid calculation: {calc}'))

        url = (f'https://www.alphaPvantage.co/timeseries/running_analytics?'
               f'SYMBOLS={symbols}&'
               f'RANGE={range}&'
               f'INTERVAL={interval}&'
               f'WINDOW={window}&'
               f'CALCULATIONS={calculations}&'
               f'APIKEY={apikey}')

        try :
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()


            self.stdout.write(self.style.SUCCESS(f'Successfully fetched data for {symbols})'))
            self.stdout.write(self.style.SUCCESS(str(data)))

        except requests.exceptions.HTTPError as http_err:
            self.stdout.write(self.style.ERROR(f'HTTP error occurred: {http_err}'))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f'An error occurred: {err}'))