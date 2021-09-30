from secret import Secret
from tiingo import TiingoClient
import pandas as pd 
from pprint import pprint
client = TiingoClient(Secret.config)
from datetime import datetime

start = '2021-01-01'
end = datetime.now().strftime("%Y-%m-%d")
symbols = ['VOO', 'SPY', 'IVV', 'SWPPX']

for symbol in symbols:
    prices = client.get_ticker_price(
                                    symbol,
                                    fmt='json',
                                    frequency='daily',
                                    startDate=start,
                                    endDate=end)
    price_sheet = pd.DataFrame.from_dict(prices)
    price_sheet['date'] = price_sheet['date'].str.rstrip('T00:00:00.000Z')
    print(price_sheet.head())
    price_sheet.to_csv('data/{}.csv'.format(symbol))
