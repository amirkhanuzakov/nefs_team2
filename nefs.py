import pandas as pd
import ta
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Download data
data = pd.read_csv('stock_data.csv')
data['Date'] = pd.to_datetime(data['Date']) # convert date column to datetime format

# Calculate the simple moving average and standard deviation with a rolling window
data['SMA'] = data['Close'].rolling(window=20).mean()
data['STDDEV'] = data['Close'].rolling(window=20).std()

# Calculate the upper and lower bands using the 95% confidence interval
data['Upper_Band'] = data['SMA'] + 1.96 * data['STDDEV']
data['Lower_Band'] = data['SMA'] - 1.96 * data['STDDEV']

# Create the plot and add lines
fig, ax = plt.subplots(figsize=(10,5))
sma_line, = ax.plot(data['Date'], data['SMA'], label='SMA')
ub_line, = ax.plot(data['Date'], data['Upper_Band'], label='Upper Band')
lb_line, = ax.plot(data['Date'], data['Lower_Band'], label='Lower Band')
close_line, = ax.plot(data['Date'], data['Close'], label='Close')

# Set up the checkbutton widget
rax = plt.axes([0.01, 0.9, 0.1, 0.1])
check = CheckButtons(rax, ('Close','SMA', 'Upper Band', 'Lower Band'), (True, True, True, True))

# Define the callback function to toggle the display of the lines
def func(label):
    if label == 'Close':
        close_line.set_visible(not close_line.get_visible())
    elif label == 'SMA':
        sma_line.set_visible(not sma_line.get_visible())
    elif label == 'Upper Band':
        ub_line.set_visible(not ub_line.get_visible())
    elif label == 'Lower Band':
        lb_line.set_visible(not lb_line.get_visible())
    plt.draw()

# Register the callback function with the checkbutton
check.on_clicked(func)

# Add plot details
ax.legend(loc='upper left')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Bollinger Bands')
plt.xticks(rotation=45) # rotate x-axis labels for better visibility

# Show the plot
plt.show()
