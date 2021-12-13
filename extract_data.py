from secret import Secret
from tiingo import TiingoClient
import pandas as pd 
client = TiingoClient(Secret.config)
from datetime import datetime

start_train = '2021-01-01'
end_train = '2021-11-16'

start_test = '2021-11-16'
# end_test = datetime.now().strftime("%Y-%m-%d")
end_test = '2021-12-08'

symbols = ['ETHUSD', 'SHIBUSD', 'BTCUSD', 'DOGEUSD']

for symbol in symbols:
    prices = client.get_ticker_price(
                                    symbol,
                                    fmt='json',
                                    frequency='daily',
                                    # startDate=start_train,
                                    # endDate=end_train,
                                    startDate=start_test,
                                    endDate=end_test
                                    )
    
    price_sheet = pd.DataFrame.from_dict(prices)
    price_sheet['date'] = price_sheet['date'].str.rstrip('T00:00:00.000Z')
    # print(price_sheet.head())
    # price_sheet.to_csv('data/{}.csv'.format(symbol))
    price_sheet.to_csv('test_data/{}.csv'.format(symbol))
