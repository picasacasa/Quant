# coding: utf-8
from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd

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

def get_eastmoney_industry_reports(pages):
    # 取回东方财富通行业报告函数
    
    from bs4 import BeautifulSoup
    import requests
    import urllib
    import pandas as pd
    
    soup2 = []
    for i in range(1, pages+1):
        html_doc = urllib.request.urlopen(page_url + str(i)).read()
        print('第' + str(i) + '页提取成功')
        soup0 = BeautifulSoup(html_doc, "lxml")
        soup1 = soup0.text[3:][:-3].split('","')
        for j in range(0, len(soup1)): #此处不能用len(soup1)-1,会缺少数据
            soup2.append(soup1[j].replace('&sbquo;', '，').replace('&quot;', '\"').split(','))
    
    dataf = pd.DataFrame(soup2,)
    # 返回DataFrame
    return dataf

def get_eastmoney_report(urls):
    from dateutil.parser import parse
    # 此处待添加验证 urls 是否为 DataFrame
    for i in range(0, len(urls)):
        temp_url = 'http://data.eastmoney.com/report/' + parse(spyl.loc[spyl.index[i]][1]).strftime('%Y'+'%m'+'%d') + '/hy,' + spyl.loc[spyl.index[i]][2] + '.html'
        temp_name = '/home/wangshi/script/' + parse(spyl.loc[spyl.index[i]][1]).strftime('%Y'+'%m'+'%d') + '_' + spyl.loc[spyl.index[i]][4] + '_' + spyl.loc[spyl.index[i]][9] + '.pdf'
        urllib.request.urlretrieve(temp_url, temp_name)
    print('Download Successfully')
    return

    
