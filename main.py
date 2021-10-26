import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
from sklearn.linear_model import LogisticRegression
import datetime
style.use('seaborn')


df = pd.read_csv('data/SPY.csv')

# get the log returns of buying and holding
price = df['close']
price_next_day = df['close'].shift(1)
df['log_returns'] = np.log(price/price_next_day)
returns = df['log_returns']
df.rename(columns = {'Unnamed: 0':'day'}, inplace = True)


df.dropna(inplace=True)
df['market_position'] = np.sign(df['log_returns'])
# date = np.array(datetime.datetime(df['date']))
# print(type(date[0]))
day = np.array(df['day'].astype('float')).reshape(1, -1).T     
position = df['market_position']

print(df)

lg_model = LogisticRegression()

lg_model.fit(day, position)
prediction = lg_model.predict(day)
plt.figure(10, 6)
plt.plot(day, position, 'g', label='data')
plt.plot(day, prediction, 'b', label= 'prediction')
plt.show()
# print(df)




