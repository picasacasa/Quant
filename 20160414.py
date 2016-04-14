import tushare as ts
import numpy as np
import matplotlib as plt

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
gp2[0] = gp2[0].toordinal() #取日期的值
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




import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from dateutil.parser import parse


gp1 = ts.get_hist_data('150131')
gp1.insert(0, 'date', gp1.index)
gp2 = gp1.T[:5].T.sort()


#######################################################
parse(gp2.iloc[0].date)
parse(gp2.iloc[0].date).date()
parse(gp2.iloc[0].date).date().toordinal()
float(parse(gp2.iloc[0].date).date().toordinal())
#######################################################
for i in range(0,len(gp2.index)):
    gp2.iloc[i].date = float(parse(gp2.iloc[i].date).date().toordinal())
    
list1 = []
for i in range(0,len(gp2.index)):
    list1.append(tuple(gp2.iloc[i]))
    
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
    
    
fig = plt.figure()
ax1=fig.add_subplot(1,1,1)
candlestick_ohlc(ax1, list1, width=1, colorup = 'r', colordown='g')

fig = plt.figure()
ax1 = list(gp2.index)
candlestick_ohlc(ax1, list1, width=1, colorup = 'r', colordown='g')

fig = plt.figure()
candlestick_ohlc(gp2.index, list1, width=1, colorup = 'r', colordown='g')

#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

quotes = list1
if len(quotes) == 0:
    raise SystemExit

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)

#plot_day_summary(ax, quotes, ticksize=3)
candlestick_ohlc(ax, list1[-100:], width=0.6, colorup = 'r', colordown='g')

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()

###Question 没有数据的周六日在图像上是有显示的
http://www.financecomputing.net/wordpress/?p=1093
