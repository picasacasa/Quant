
# coding: utf-8

# In[1]:

sw_code = '801120'


# In[2]:

def get_sw_industry_list(industry_code): # 不用 list ，用 text 输入
    
    # 引入所需包
    from bs4 import BeautifulSoup
    import requests
    import urllib
    import pandas as pd
    
    # 读取数据文件
    html_doc = urllib.request.urlopen('http://www.swsindex.com/downfile.aspx?code=' + industry_code).read()
    
    # 用 lmxl 解析数据文件
    soup0 = BeautifulSoup(html_doc, "lxml")
    
    # 分离出 table
    table1 = soup0.find_all('table')[0]
    
    # 准备 list1、list2 两个空 list 备用
    list1 = []
    list2 = []
    
    # 处理 th 即标题
    
    for i in range(0, len(table1.find_all('th'))):
        list2.append(table1.find_all('th')[i].text)
        
    # 将标题存入 list1
    list1.append(list2)
    
    # 再次将 list2 清空
    list2 = []
    
    # 第一层循环，依次读取每一行 tr
    for i in range(1, len(table1.find_all('tr'))):
        
        # 每次将 list2 清空备用
        list2 = []
        
        # 第二层循环，读取每个 td 元素，其 text 依次存入 list2
        for j in table1.find_all('tr')[i].find_all('td'):
            list2.append(j.text)
            
        # 将写入的 list2 文件附加到 list1,循环完成即生成包函完整数据的 list1
        list1.append(list2)
        
    # 整理生成的 DataFrame
    datatemp = pd.DataFrame(list1[1:], columns = list1[0])
    datatemp.index = datatemp['证券代码']
    datatemp.index.name = 'code'
    datatemp['文件夹'] = '/home/wangshi/reports/stock_reports/' + industry_code + '/' + datatemp['证券代码'] + '_' + datatemp['证券名称'] + '/'
    
    
    # 返回股票清单 DataFrame, 后用 list 函数返回
    return datatemp


# In[ ]:

# 此处用 list 输入 codes，可试用 list + DataFrame 输入
def get_eastmoney_stock_report(urls, paths):
    
    # 下载个股
    from dateutil.parser import parse
    from bs4 import BeautifulSoup
    import requests, urllib, os, shutil, json
    import pandas as pd
    
    # 此处待添加验证 urls 是否为 DataFrame
    count_download = 0
    count_pass = 0
    count_fail = 0
    for i in range(0, len(urls)):
        temp_url = 'http://data.eastmoney.com/report/' + parse(urls.loc[urls.index[i]]['datetime']).strftime('%Y'+'%m'+'%d') + '/' + urls.loc[urls.index[i]]['infoCode'] + '.html'
        # print(temp_url)
        html_doc = urllib.request.urlopen(temp_url).read()
        soup = BeautifulSoup(html_doc, "lxml")
        try:
            file_url = soup.find_all(text = '查看PDF原文')[0].parent.get('href')
            temp_name = paths + parse(urls.loc[urls.index[i]]['datetime']).strftime('%C'+'%m'+'%d') + '_' + urls.loc[urls.index[i]]['insName'] + '_' + urls.loc[urls.index[i]]['title'] + '.pdf'
        
            if os.path.isfile(temp_name) == True:
                # print('File already exist! PASS!')
                count_pass += 1
                pass
            else:
                urllib.request.urlretrieve(file_url, temp_name)
                count_download += 1
                # print('Download ' + str(count_download) + '/' + str(len(urls)) + ' new files '+ 'Successfully !')
        except:
            print('Fail to get the file. ' + 'Please download the file manually !' + '\n'  + temp_url)
            count_fail += 1
            pass
        
    print('    DOWN: ' + str(count_download) + '/' + str(len(urls)) + '\n'  + '    PASS: ' + str(count_pass) + '/' + str(len(urls)) + '\n'   + '    FAIL: ' + str(count_fail) + '/' + str(len(urls)))

    return


# In[3]:

df = get_sw_industry_list(sw_code)


# In[5]:

df[:1]


# In[ ]:

def get_stock_report_list(stock_codes, path):
    # path 为保存数据的位置，非报告下载位置
    
    from bs4 import BeautifulSoup
    from math import ceil
    import requests, urllib, os, shutil, json
    import pandas as pd
    
    
    
    # 第一层循环，遍历列表中每个股票代码，取得其报告页数
    for stock_code in stock_codes:
        
        try:
            url_data_0 = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=1&code=' + stock_code
            html_doc_0 = urllib.request.urlopen(url_data_0).read()
            soup_0 = BeautifulSoup(html_doc_0, "lxml")
        
            # 用 json 处理得到的 json 文本
            jsontext_0 = json.loads(soup_0.text.split('=')[1])
        
            # 向上取整取得报告页数
            page_numbers = ceil(int(jsontext_0['count'])/25)
        
            data_0 = []
        
            # 第二层循环，遍历股票报告页面，取得其报告编码
            for page_number in range(1, page_numbers + 1):
            
                url_data_1 = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=' + str(page_number) + '&code=' + stock_code
                html_doc_1 = urllib.request.urlopen(url_data_1).read()
                soup_1 = BeautifulSoup(html_doc_1, "lxml")
            
                # 用 json 处理得到的 json 文本
                jsontext_1 = json.loads(soup_1.text.split('=')[1])
            
                #合并新的列表
                data_0 += jsontext_1['data']
        
            #处理取得的编码为DataFrame，并将结果存盘
            data_1 = pd.DataFrame(data_0)
            data_1.index = data_1['infoCode']
            data_1.index.name = 'infoCodes' # 为避免名称重复这里设置为 infoCodes
            
            
            data_1.to_csv(path + stock_code)
        
        except:
            print('Fail to get reports of ' + stock_code)

    return

