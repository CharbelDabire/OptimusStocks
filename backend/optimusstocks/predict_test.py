import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from stock_service import StockService

# Load environment variables
load_dotenv()

# Set up API keys and initialize StockService
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
if not ALPHA_VANTAGE_API_KEY:
    raise ValueError('No Alpha Vantage API Key found')

stock_service = StockService(api_key=ALPHA_VANTAGE_API_KEY)

# Define ticker symbol to fetch data for 
ticker = "TSLA"

# fetch data from Yahoo Finance
quote_table = stock_service.get_quote_table(ticker)
print('Quote Table:', quote_table) 

# fetch historical data from YFinance
historical_data = stock_service.get_historical_data(ticker, period='5mo')
print('Historical Data:', historical_data)

# Fetch Company Overview info from Alpha Vantage
company_overview = stock_service.get_company_overview(ticker)
print('Company Overview:', company_overview)

# Convert historical data to a pandas DataFrame
historical_df = pd.DataFrame(historical_data)
print(historical_df)

# Plot historical closing prices
plt.figure(figsize=(10, 5))
plt.plot(historical_df.index, historical_df['Close'], label='Close Price')
plt.title(f'{ticker} Historical Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()


# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(historical_df['Close'].values.reshape(-1, 1))

# Plot the normalized data
plt.figure(figsize=(10, 5))
plt.plot(historical_df.index, scaled_data, label='Normalized Close Price')
plt.title(f'{ticker} Normalized Closing Prices')
plt.xlabel('Date')
plt.ylabel('Normalized Closing Price')
plt.legend()
plt.show()





