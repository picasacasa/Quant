import tushare as ts
import numpy as np
import matplotlib.plot as plt
import matplotlib as plt
%hist
gp = ts.get_hist_data('150131')
gp = gp.sort()
gp.head
gp.loc
gp.loc()
gp.icol
plt.plot(gp.close.values)
import matplotlib.pyplot as plt
plt.plot(gp.close.values)
plt.show()
plt.plot(gp.close.values[-50:])
plt.show()
plt.plot(gp.close.values[-50:])
plt.plot(gp.open.values[-50:])
plt.show()
plt.plot((gp.open.values[-50:]+gp.close.values[-50:])/2)
plt.show()
plt.plot(gp.low.values[-50:])
plt.plot(gp.high.values[-50:])
plt.show()
from matplotlib.dates import DateFormatter, Weekdaylocator, DayLocator, MONDAY
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
%paste
%paste
%paste
%paste
quotes
type(quotes)
type(quotes[0])
quotes[0]
gp
gp.open
fig = plt.figure()
ax1=fig.add_subplot(1,1,1)
ax1.set_title('150131')
quotes = [gp.index, gp.open, gp.high, gp.low, gp.close]
quotes[-10:]
quotes[-1:]
quotes[-1:]
candlestick_ohlc(ax1, gp, width=1, colorup = 'r', colordown='g')
gp[:5]
gp.open[-1]
gp.open[-10:]
type(gp)
gp.insert(0,'date',gp.index)
gp
gp.open[-10:]
gp[-5:]
candlestick_ohlc(ax1, gp, width=1, colorup = 'r', colordown='g')
from dateutil.parser import parse
parse(gp.date)
parse(gp.date[0])
type(gp.date)
parse(gp.index)
parse(gp.index[0])
del gp['date']
gp[-5:]
gp.insert(0,'date',parse(gp.index))
pd.index.to_datetime
gp.index.to_datetime
gp.index.to_datetime[0]
type(gp.index.to_datetime)
type(gp.index[0].to_datetime)
gp.index.to_datetime[0]
gp.index.to_datetime
gp.index
type(gp.index)
type(parse(gp.index))
parse(gp.index)
import pandas as pd
parse(gp.index)
gp.index.to_datetime
pd.to_datetime(gp.index)
gp.insert(0,'date',pd.to_datetime(gp.index))
gp
gp[-5:]
candlestick_ohlc(ax1, gp, width=1, colorup = 'r', colordown='g')
type(gp.index[0])
type(gp.date[0])
gp.date[0]
gp.T
type(gp.T)
gp.T[0]
gp.T[-1:]
gp
gp.T[0]
type(gp.T)
type(gp)
gp.date[0]
gp.date.tolist()
gp.date.tolist()[0]
gp[0]
gp[-5:]
gp.T
gp.T
gp.date['2016-04-12']
gp.date.close
gp.date.close()
gp.date['close']
gp.T
gp.T['close']
gp.T[-1:]
gp.T[:5]
gp.T[:5].T
gp.T[:5].T['2016-04-14']
gp.T[:5].T
gp1 = gp.T[:5].T
gp1[index = '2016-04-14']
gp1.ix['2016-04-14']
gp1.ix['2016-04-14'].tolist()
gp2 = gp1.ix['2016-04-14'].tolist()
gp2
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
gp2[0]
gp2[0].value
gp2[0].date
gp2[0].date()
gp2[0].date().value
gp2[0].date().value()
gp2[0] = gp2[0].date().value()
gp2[0]
gp2[0] = gp2[0].date().value()
gp2[0] = gp2[0].date()
gp2
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
gp2[0] = gp2[0].date()
gp2[0]
gp2[0].bashrc
gp2[0].bashrc()
gp2[0].value
gp2[0].value()
gp2[0]-1
gp2[0]
datetime.date,today()
import datetime
datetime.date,today()
datetime.date.today()
datetime.date.today()-gp2[0]
gp2[0] = gp2[0].toordinal()
gp2
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
gp2[0]
gp2[0] * 2
gp2
tuple(gp2)
gp2
gp3 = tuple(gp2)
gp2
gp3
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
l1 = []
l1.append(gp3)
l
l1
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
l1[:5]
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
l1 = []
l1
gp3[0]
float(gp3[0])
gp3[0] = float(gp3[0])
gp2[0] = float(gp2[0])
gp3 = tuple(gp2)
gp3
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1.append(gp3)
l1
candlestick_ohlc(ax1, gp2, width=1, colorup = 'r', colordown='g')
%paste
%paste
%paste
candlestick_ohlc(ax, l1, width=0.6)
plt.show()
%hist
%history
