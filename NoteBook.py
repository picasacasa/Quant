import numpy as np
import pandas as pd
import tushare as ts
import seaborn as sns

#利用TuShare获取数据
g000538 = ts.get_hist_data('000538')
g000538.index[0] = '2016-03-04' #srting

#将格式的时间文本转换为时间或日期
from dateutil.parser import parse 
parse(g000538.index[0]) = datetime.datetime(2016, 3, 4, 0, 0)

