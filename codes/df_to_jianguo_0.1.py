
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd


# In[2]:

# 东方财富通页面地址后缀格式
page_list = ['x', 'y', 'z', '0', '1', '2', '3', '4', '5','xMA==', 'xMQ==',]


# In[3]:

# 东方财富通页面地址前缀格式
page_url = 'http://data.eastmoney.com/report/hyyb.html#dHA9MCZjZz0wJmR0PTImcGFnZT0'


# In[4]:

pages = []
for i in page_list:
    pages.append(page_url + i)
pages


# soup3 = []
# for i in page_list:
#     html_doc = urllib.request.urlopen(page_url + i).read()
#     soup = BeautifulSoup(html_doc, "lxml")
#     soup1 = str(soup.find_all('script'))
#     soup2 = soup1.split(':["')[1].split('"]')[0].split('","')
#     for j in range(0, len(soup2)-1):
#         soup3.append(soup2[j].replace('&sbquo;', '，').replace('&quot;', '\"').split(','))
# 

# In[5]:

soup3 = []
for i in range(0, len(pages)-1):
    html_doc = ''
    html_doc = urllib.request.urlopen(pages[i]).read()
    print(type(html_doc), len(html_doc))
    soup = BeautifulSoup(html_doc, "lxml")
    soup1 = str(soup.find_all('script'))
    soup2 = soup1.split(':["')[1].split('"]')[0].split('","')
    for j in range(0, len(soup2)-1):
        soup3.append(soup2[j].replace('&sbquo;', '，').replace('&quot;', '\"').split(','))


# In[6]:

dataf = pd.DataFrame(soup3,)
dataf.to_csv('/home/wangshi/script/dfcft_hy')


# In[14]:

html_doc = ''
html_doc = urllib.request.urlopen('http://data.eastmoney.com/report/hyyb.html#dHA9MCZjZz0wJmR0PTImcGFnZT0x',).read()
print(type(html_doc), len(html_doc))
soup = BeautifulSoup(html_doc, "lxml")
soup1 = str(soup.find_all('script'))
soup2 = soup1.split(':["')[1].split('"]')[0].split('","')
for j in range(0, len(soup2)-1):
    soup3.append(soup2[j].replace('&sbquo;', '，').replace('&quot;', '\"').split(','))


# In[11]:

html_doc = ''
html_doc = urllib.request.urlopen('http://data.eastmoney.com/report/hyyb.html#dHA9MCZjZz0wJmR0PTImcGFnZT0y').read()
print(type(html_doc), len(html_doc))
soup = BeautifulSoup(html_doc, "lxml")
soup1 = str(soup.find_all('script'))
soup2 = soup1.split(':["')[1].split('"]')[0].split('","')
for j in range(0, len(soup2)-1):
    soup3.append(soup2[j].replace('&sbquo;', '，').replace('&quot;', '\"').split(','))


# In[12]:

html_doc = ''
html_doc = urllib.request.urlopen('http://data.eastmoney.com/report/hyyb.html#dHA9MCZjZz0wJmR0PTImcGFnZT0z').read()
print(type(html_doc), len(html_doc))
soup = BeautifulSoup(html_doc, "lxml")
soup1 = str(soup.find_all('script'))
soup2 = soup1.split(':["')[1].split('"]')[0].split('","')
for j in range(0, len(soup2)-1):
    soup3.append(soup2[j].replace('&sbquo;', '，').replace('&quot;', '\"').split(','))


# In[ ]:



