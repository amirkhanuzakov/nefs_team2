import pandas as pd
import ta
import matplotlib.pyplot as plt

# Load the stock data into a pandas DataFrame
df = pd.read_csv('stock_data.csv')


# calculate 20-day SMA and 50-day SMA
df['SMA20'] = ta.trend.sma_indicator(df['Close'], window=20)
df['SMA50'] = ta.trend.sma_indicator(df['Close'], window=50)

# calculate 12-day EMA and 26-day EMA
df['EMA12'] = ta.trend.ema_indicator(df['Close'], window=12)
df['EMA26'] = ta.trend.ema_indicator(df['Close'], window=26)

# calculate 14-day RSI
df['RSI14'] = ta.momentum.rsi(df['Close'], window=14)

# Calculate the MACD and signal lines using the signal() function
df['MACD'] = ta.trend.macd_diff(df['Close'], window_slow=26, window_fast=12)
df['Signal'] = ta.trend.macd_signal(df['Close'], window_slow=26, window_fast=12, window_sign=9)

# print the DataFrame with SMA, EMA, RSI, and MACD indicators
print(df)


# Create a line plot of the MACD and signal lines
plt.plot(df['Date'], df['MACD'], label='MACD')
plt.plot(df['Date'], df['Signal'], label='Signal')
plt.legend()
plt.xlabel('Date')
plt.ylabel('MACD/Signal')
plt.title('MACD and Signal Lines')
plt.show()
