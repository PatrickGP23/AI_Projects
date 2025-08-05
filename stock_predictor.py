import yfinance as yf

import matplotlib.pyplot as plt

ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2023-01-01')

plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Closing Price')
plt.title(f'{ticker} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()