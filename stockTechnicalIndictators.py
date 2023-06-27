import pandas as pd
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

api = 'PSPQT90UH1IK7XV3'
freq = 60

indicators = TechIndicators(key=api, output_format='pandas')

data_rsi, meta_data_rsi = indicators.get_rsi(symbol='NVDA', interval='1min', time_period=freq, series_type='close')

data_sma, meta_data_sma = indicators.get_sma(symbol='NVDA', interval='1min', time_period=freq, series_type='close')

data_vol, meta_data_vol = indicators.get_intraday(symbol='NVDA', interval='1min', outputsize = 'full')

#i = 1
#while i==1:
#	data_vol, meta_data_vol = indicators.get_intraday(symbol='NVDA', interval='1min', outputsize = 'full')
#	data.to_excel("output.xlsx")
#	time.sleep(60)

close_data = data_vol['4. close']
percent_diff = close_data.pct_change()
last = percent_diff[-1]
if abs(last) > 0.0001:
	print("NVDA:" + last)


dfA = data_sma.iloc[1::]
dfB = data_rsi
dfA.idex = dfB.index





fig, ax1 = plt.subplots()
ax1.plot(dfA, 'blue')
ax2 = ax1.twinx()
ax2.plot(dfB, 'red')
plt.title("SMA and RSI Graph of NVIDIA Historical Market Data") 

plt.show()
