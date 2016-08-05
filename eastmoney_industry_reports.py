# coding: utf-8
from bs4 import BeautifulSoup
import requests
import urllib

# 东方财富通页面地址后缀格式，可用range代替
page_number = 10

# 东方财富通页面地址前缀格式, 感谢http://www.mamicode.com/info-detail-1325623.html
page_url = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=HYSR&mkt=0&stat=0&cmd=2&code=&sc=&ps=50&p=''


soup2 = []
for i in range(1, page_number+1):
    html_doc = ''
    html_doc = urllib.request.urlopen(page_url + str(i)).read()
    print('第' + str(i) + '页提取成功')
    soup0 = BeautifulSoup(html_doc, "lxml")
    soup1 = soup.text[3:][:-3].split('","')
    for j in range(0, len(soup1)-1):
        soup2.append(soup1[j].replace('&sbquo;', '，').replace('&quot;', '\"').split(','))

dataf = pd.DataFrame(soup2,)
dataf.to_csv('/home/wangshi/script/dfcft_hy')
