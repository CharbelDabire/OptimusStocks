import requests
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetch technical indicators for given stock symbol'

    FUNCTION_CHOICES = [
        'SMA','EMA','WMA','DEMA','TEMA','TRIMA','KAMA','MAMA',
        'T3','MACDEXT','STOCH','STOCHF','RSI','STOCHRSI','WILLR',
        'ADX','ADXR','APO','PPO','MOM','BOP','CCI','CMO','ROC',
        'ROCR','AROON','AROONOSC','MFI','TRIX','ULTOSC','DX',
        'MINUS_DI','PLUS_DI','MINUS_DM','PLUS_DM','BBANDS',
        'MIDPOINT','MIDPRICE','SAR','TRANGE','ATR','NATR',
        'AD','ADOSC','OBV','HT_TRENDLINE','HT_SINE','HT_TRENDMODE',
        'HT_DCPERIOD','HT_DCPHASE','HT_PHASOR']

    """ 
    Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 
    1 = Exponential Moving Average (EMA), 
    2 = Weighted Moving Average (WMA), 
    3 = Double Exponential Moving Average (DEMA), 
    4 = Triple Exponential Moving Average (TEMA), 
    5 = Triangular Moving Average (TRIMA), 
    6 = T3 Moving Average, 
    7 = Kaufman Adaptive Moving Average (KAMA), 
    8 = MESA Adaptive Moving Average (MAMA).
    """
    timePeriodSet =  {'SMA', 'EMA', 'WMA', 'DEMA', 'TEMA', 'TRIMA', 'KAMA', 'T3', 'RSI', 'STOCHRSI', 'WILLR', 'ADX', 'ADXR', 
                    'MOM', 'CCI', 'CMO', 'ROC', 'ROCR', 'AROON', 'AROONOSC', 'MFI', 'TRIX', 'DX', 'MINUS_DI', 'PLUS_DI', 
                    'MINUS_DM', 'PLUS_DM', 'BBANDS', 'MIDPOINT', 'MIDPRICE', 'ATR', 'NATR'}
    
    seriesTypeSet =  {'SMA', 'EMA', 'WMA', 'DEMA', 'TEMA', 'TRIMA', 'KAMA', 'MAMA', 'MACDEXT', 'RSI', 'STOCHRSI', 'APO', 'PPO','MOM',
                   'CMO', 'ROC', 'ROCR', 'TRIX', 'BBANDS', 'MIDPOINT', 'HT_TRENDLINE', 'HT_SINE', 'HT_TRENDMODE', 'HT_DCPERIOD', 
                   'HT_DCPHASE','HT_PHASOR'} 

    

    def add_arguments(self, parser):
        parser.add_argument('function', type=str, choices= self.FUNCTION_CHOICES, help='Function of your choice (e.g. SMA, EMA, RSI)')
        parser.add_argument('symbol', type=str, help='Stock symbol for which you want technical indicators')
        parser.add_argument('interval', type=str, choices=['1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'], default='daily', help='Interval of your choice (daily by default)')
        parser.add_argument('--time_period', type=int, default=14, help='Number of data points used to calculate each indicator')
        parser.add_argument('--series_type', type=str, choices=['close', 'open', 'high', 'low'], default='close', help='Price type of your choice (close by default)')
        parser.add_argument('--month', type=str, help='Month of your choice (use only for intraday intervals, in YYYY-MM format)')
        parser.add_argument('--datatype', type=str, choices=['json', 'csv'], default='json', help=' data type of your choice (json by default)')
        parser.add_argument('--fastlimit', type=float, default=0.01, help='Fast limit for adaptive moving average')
        parser.add_argument('--slowlimit', type=float, default=0.01, help='Slow limit for adaptive moving average')
        parser.add_argument('--fastperiod', type=int, default=12, help='Fast period for MACDEXT, APO, PPO, ADOSC')
        parser.add_argument('--slowperiod', type=int, default=26, help='Slow period for MACDEXT, APO, PPO, ADOSC')
        parser.add_argument('--signalperiod', type=int, default=9, help='Signal period for MACDEXT')
        parser.add_argument('--fastmatype', type=int, default=0, help='Fast moving average type for MACDEXT')
        parser.add_argument('--slowmatype', type=int, default=0, help='Slow moving average type for MACDEXT')
        parser.add_argument('--signalmatype', type=int, default=0, help='Signal moving average type for MACDEXT')
        parser.add_argument('--fastkperiod', type=int, default=5, help='Fast %K period for STOCH, STOCHF, STOCHRSI')
        parser.add_argument('--slowkperiod', type=int, default=3, help='Slow %K period for STOCH')
        parser.add_argument('--slowdperiod', type=int, default=3, help='Slow %D period for STOCH')
        parser.add_argument('--slowkmatype', type=int, default=0, help='Slow %K moving average type for STOCH')
        parser.add_argument('--slowdmatype', type=int, default=0, help='Slow %D moving average type for STOCH')
        parser.add_argument('--fastdperiod', type=int, default=3, help='Fast %D period for STOCHF, STOCHRSI')
        parser.add_argument('--fastdmatype', type=int, default=0, help='Fast %D moving average type for STOCHF, STOCHRSI')
        parser.add_argument('--matype', type=int, default=0, help='Moving average type for APO, PPO, BBANDS')
        parser.add_argument('--timeperiod1', type=int, default=7, help='Time period for first moving average for ULTOSC')
        parser.add_argument('--timeperiod2', type=int, default=14, help='Time period for second moving average for ULTOSC')
        parser.add_argument('--timeperiod3', type=int, default=28, help='Time period for third moving average for ULTOSC')
        parser.add_argument('--nbdevup', type=int, default=2, help='Standard deviation multiplier for upper band for BBANDS')
        parser.add_argument('--nbdevdn', type=int, default=2, help='Standard deviation multiplier for lower band for BBANDS')
        parser.add_argument('--acceleration', type=float, default=0.01, help='Acceleration factor for SAR')
        parser.add_argument('--maximum', type=float, default=0.2, help='Maximum acceleration factor for SAR')

    def handle(self, *args, **kwargs):
        function = kwargs['function']
        symbol = kwargs['symbol']
        interval = kwargs['interval']
        time_period = kwargs.get('time_period', 14)
        series_type = kwargs.get('series_type')
        month = kwargs.get('month')
        datatype = kwargs.get('datatype', 'json')
        fast_limit = kwargs.get('fastlimit', 0.01)
        slow_limit = kwargs.get('slowlimit', 0.01)
        fast_period = kwargs.get('fastperiod', 12)
        slow_period = kwargs.get('slowperiod', 26)
        signal_period = kwargs.get('signalperiod', 9)
        fast_ma_type = kwargs.get('fastmatype', 0)
        slow_ma_type = kwargs.get('slowmatype', 0)
        signal_ma_type = kwargs.get('signalmatype', 0)
        fast_k_period = kwargs.get('fastkperiod', 5)
        slow_k_period = kwargs.get('slowkperiod', 3)
        slow_d_period = kwargs.get('slowdperiod', 3)
        slow_k_ma_type = kwargs.get('slowkmatype', 0)
        slow_d_ma_type = kwargs.get('slowdmatype', 0)
        fast_d_period = kwargs.get('fastdperiod', 3)
        fast_d_ma_type = kwargs.get('fastdmatype', 0)
        ma_type = kwargs.get('matype', 0)
        time_period1 = kwargs.get('timeperiod1', 7)
        time_period2 = kwargs.get('timeperiod2', 14)
        time_period3 = kwargs.get('timeperiod3', 28)
        nbdevup = kwargs.get('nbdevup', 2)
        nbdevdn = kwargs.get('nbdevdn', 2)
        acceleration = kwargs.get('acceleration', 0.01)
        maximum = kwargs.get('maximum', 0.2)
        api_key = settings.ALPHA_VANTAGE_API_KEY

        url_base = 'https://www.alphavantage.co/query?'
        params = {
            'function': function,
            'symbol': symbol,
            'interval': interval,
            'apikey': api_key
        }

        if time_period and function in self.timePeriodSet:
            params['time_period'] = time_period
        if series_type and function in self.seriesTypeSet:
            params['series_type'] = series_type
        if interval in {'1min', '5min', '15min', '30min', '60min'} and month:
            params['month'] = month
        if datatype:
            params['datatype'] = datatype
        if function == 'MAMA':
            if fast_limit:
                params['fastlimit'] = fast_limit
            if slow_limit:
                params['slowlimit'] = slow_limit
        if function in {'MACDEXT', 'APO', 'PPO', 'ADOSC'}:
            params['fastperiod'] = fast_period
            params['slowperiod'] = slow_period
        if function == 'MACDEXT':
            if signal_period:
                params['signalperiod'] = signal_period
            if fast_ma_type:
                params['fastmatype'] = fast_ma_type
            if slow_ma_type:
                params['slowmatype'] = slow_ma_type
            if signal_ma_type:
                params['signalmatype'] = signal_ma_type
        if function in {'STOCH', 'STOCHF', 'STOCHRSI'}:
            if fast_k_period:
                params['fastkperiod'] = fast_k_period
        if function == 'STOCH':
            if slow_k_period:
                params['slowkperiod'] = slow_k_period
            if slow_d_period:
                params['slowdperiod'] = slow_d_period
            if slow_k_ma_type:
                params['slowkmatype'] = slow_k_ma_type
            if slow_d_ma_type:
                params['slowdmatype'] = slow_d_ma_type
        if function in {'STOCHF', 'STOCHRSI'}:
            if fast_d_period:
                params['fastdperiod'] = fast_d_period
            if fast_d_ma_type:
                params['fastdmatype'] = fast_d_ma_type
        if function in {'APO', 'PPO', 'BBANDS'}:
            if ma_type:
                params['matype'] = ma_type
        if function == 'ULTOSC':
            if time_period1:
                params['timeperiod1'] = time_period1
            if time_period2:
                params['timeperiod2'] = time_period2
            if time_period3:
                params['timeperiod3'] = time_period3
        if function == 'BBANDS':
            if nbdevup:
                params['nbdevup'] = nbdevup
            if nbdevdn:
                params['nbdevdn'] = nbdevdn
        if function == 'SAR':
            if acceleration:
                params['acceleration'] = acceleration
            if maximum:
                params['maximum'] = maximum


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
            
            
            
            
            

        
        