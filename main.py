import ccxt
import pandas as pd
import matplotlib.pyplot as plt

exchange = ccxt.binance()

bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=500)

df = pd.DataFrame(bars, columns=['time','open','high','low','close','volume'])
df['time'] = pd.to_datetime(df['time'], unit='ms')

# plt.plot(df['time'], df['close'])
# plt.show()
#
print (df.head())
