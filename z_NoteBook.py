import numpy as np
import pandas as pd
import tushare as ts
import seaborn as sns
import matplotlib.pyplot as plt

#利用TuShare获取数据
g000538 = ts.get_hist_data('000538')
g000538.index[0] = '2016-03-04' #srting

#将格式的时间文本转换为时间或日期
from dateutil.parser import parse 
parse(g000538.index[0]) = datetime.datetime(2016, 3, 4, 0, 0)

#用sort_index排序标签列
g000538 = g000538.sort_index()

#cd定位到相应文件夹
cd /home/wangshi/pydata-book-master

#读取相应文件
!cat ch06/ex1.csv
    a,b,c,d,message
    1,2,3,4,hello
    5,6,7,8,world
    9,10,11,12,foo

#用pd.read_csv读取相关文件
pd.read_csv('ch06/ex1.csv')
       a   b   c   d message
    0  1   2   3   4   hello
    1  5   6   7   8   world
    2  9  10  11  12     foo


#pd.read_csv的用法
pd.read_table('ch06/ex1.csv',sep=',')
       a   b   c   d message
    0  1   2   3   4   hello
    1  5   6   7   8   world
    2  9  10  11  12     foo

!cat ch06/ex2.csv
    1,2,3,4,hello
    5,6,7,8,world
    9,10,11,12,foo

pd.read_csv('ch06/ex2.csv',header = None)
       0   1   2   3      4
    0  1   2   3   4  hello
    1  5   6   7   8  world
    2  9  10  11  12    foo

pd.read_csv('ch06/ex2.csv',names=['a','b','c','d','message'])
       a   b   c   d message
    0  1   2   3   4   hello
    1  5   6   7   8   world
    2  9  10  11  12     foo
    
names=['a','b','c','d','message']
pd.read_csv('ch06/ex2.csv',names=names,index_col='message')
             a   b   c   d
    message               
    hello    1   2   3   4
    world    5   6   7   8
    foo      9  10  11  12

!cat ch06/csv_mindex.csv
    key1,key2,value1,value2
    one,a,1,2
    one,b,3,4
    one,c,5,6
    one,d,7,8
    two,a,9,10
    two,b,11,12
    two,c,13,14
    two,d,15,16

pd.read_csv('ch06/csv_mindex.csv',index_col=['key1','key2'])
               value1  value2
    key1 key2                
    one  a          1       2
         b          3       4
         c          5       6
         d          7       8
    two  a          9      10
         b         11      12
         c         13      14
         d         15      16

#用to_csv保存为csv文件
g1.to_csv('ch06/temp1.csv')
