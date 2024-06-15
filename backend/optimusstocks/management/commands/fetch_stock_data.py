import requests
from django.core.management.base import BaseCommand
from optimusstocks.models import Stock
from django.conf import settings
from datetime import datetime


class Command(BaseCommand):
    help = 'Fetch  stock data from Alpha Vantage'

    def add_arguments(self, parser):
        parser.add_argument('symbol', type=str,  help='Stock symbol')
        parser.add_argument('function', type=str, choices=['TIME_SERIES_INTRADAY', 'TIME_SERIES_DAILY_ADJUSTED', 'TIME_SERIES_WEEKLY_ADJUSTED', ' TIME_SERIES_MONTHLY_ADJUSTED'], help='Time series function')
        parser.add_argument('--interval', type=str, choices = ['1min', '5min', '15min', '30min', '60min'], help='Time interval between data points')
        parser.add_argument('--adjusted', type=bool, default=True, help='Whether to retrieve adjusted data')
        parser.add_argument('--extended_hours', type=bool, default=True, help='Whether to include extending trading hours for intraday data')


    def handle(self, *args, **kwargs):
        symbol = kwargs['symbol']
        function = kwargs['function']
        interval = kwargs.get('interval')
        adjusted = kwargs['adjusted']
        extended_hours = kwargs['extended_hours']        
        api_key = settings.ALPHA_VANTAGE_API_KEY
        
        base_url = 'https://www.alphavantage.co/query?'
        params = {
            'function': function,
            'symbol': symbol,
            'apikey': api_key
        }
        
        if function == 'TIME_SERIES_INTRADAY':
            if not interval:
                self.stdout.write(self.style.ERROR('Interval is required for intraday data'))
                return 
            params['interval'] = interval
            params['adjusted'] = 'true' if adjusted else 'false'
            params['extended_hours'] = 'true' if extended_hours else 'false'
            
        url = base_url + '&'.join([f'{key}={value}' for key, value in params.items()])
        response = requests.get(url)
        data = response.json()
        
        if function == 'TIME_SERIES_INTRADAY':
            time_series_key = f'Time Series ({interval})'
        elif function == 'TIME_SERIES_DAILY_ADJUSTED':
            time_series_key = 'Daily Adjusted Time Series'
        elif function == 'TIME_SERIES_WEEKLY_ADJUSTED':
            time_series_key = 'Weekly Adjusted Time Series'
        elif function == 'TIME_SERIES_MONTHLY_ADJUSTED':
            time_series_key = 'Monthly Adjusted Time Series'
        else:
            self.stdout.write(self.style.ERROR('Invalid time series function'))
            return
        
        
        if time_series_key in data:
            time_series = data[time_series_key]
            for timestamp, values in time_series.items():
                stock_date = datetime.strptime(timestamp, '%Y-%m-%d' if function != 'TIME_SERIES_INTRADAY' else '%Y-%m-%d %H:%M:%S')
                stock, created = Stock.objects.get_or_create(
                    symbol=symbol,
                    date=stock_date,
                    defaults={
                        'open': values['1, open'],
                        'high': values['2, high'],
                        'low': values['3, low'],
                        'close': values['4, close'],
                        'volume':values['5, volume']
                    }
                )
            self.stdout.write(self.style.SUCCESS(f'Successfully fetched data for {symbol}'))
        else:
            self.stdout.write(self.style.ERROR('Error fetching data'))



