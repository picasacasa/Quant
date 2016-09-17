# coding: utf-8

from datetime import datetime
start_time = datetime.now()

print('-' * len(str(start_time)))
print(str(datetime.now()) + '\n')

from dateutil.parser import parse
from bs4 import BeautifulSoup
import requests, urllib, os, shutil, json
import pandas as pd
# 异常处理
import traceback

def get_sw_industry_list(industry_code): # 不用 list ，用 text 输入
    
    # 引入所需包
    # from bs4 import BeautifulSoup
    # import requests
    # import urllib
    # import pandas as pd
    
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
    
    for i in list(datatemp['文件夹']):
        if os.path.exists(i):  
            pass  
        else:  
            os.mkdir(i)  
    
    # 返回股票清单 DataFrame, 后用 list 函数返回
    return datatemp


# DataFrame 的差
def df_diff(df_a, df_b):
    df_a_b = df_a.ix[df_a.index.difference(df_b.index)]
    return df_a_b

# DataFrame 的并
def df_all(df_a, df_b):
    df_a_b = df_a.ix[df_a.index.difference(df_b.index)]
    df_all = df_a_b.append(df_b)
    return df_all


# 此处用 list 输入 codes，可试用 list + DataFrame 输入
def get_eastmoney_stock_report(urls, paths, code, name):
    
    # 下载个股
    # from dateutil.parser import parse
    # from bs4 import BeautifulSoup
    # import requests, urllib, os, shutil, json
    # import pandas as pd
    count_download = 0
    count_pass = 0
    count_fail = 0
    # 此处待添加验证 urls 是否为 DataFrame

    for i in range(0, len(urls)):
        try:
            temp_url_3 = 'http://data.eastmoney.com/report/' + parse(urls.loc[urls.index[i]]['datetime']).strftime('%Y'+'%m'+'%d') + '/' + urls.loc[urls.index[i]]['infoCode'] + '.html'
            html_doc_3 = urllib.request.urlopen(temp_url_3).read()
            soup_3 = BeautifulSoup(html_doc_3, "lxml")

            file_url_3 = soup_3.find_all(text = '查看PDF原文')[0].parent.get('href')
            temp_name_3 = paths + parse(urls.loc[urls.index[i]]['datetime']).strftime('%g'+'%m'+'%d') + '_' + code + '_' + name + '_' + urls.loc[urls.index[i]]['insName'] + '_' + urls.loc[urls.index[i]]['title'] + '.pdf'
        
            if os.path.isfile(temp_name_3) == True:
                # print('File already exist! PASS!')
                count_pass += 1
            else:
                urllib.request.urlretrieve(file_url_3, temp_name_3)
                count_download += 1
                # print('Download ' + str(count_download) + '/' + str(len(urls)) + ' new files '+ 'Successfully !')
        except:
            print('Fail to get the file of ' + code + '_' + name + ',' + 'Please download the file manually !' + '\n'  + temp_url_3)
            count_fail += 1
        
    if count_download + count_pass + count_fail == 0:
        pass
    else:
        print(code + '_' + name + '：' + 'DOWN:' + str(count_download) + '_' + 'PASS:' + str(count_pass) + '_' + 'FAIL:' + str(count_fail))
    
    return

# 通过输入股票代码列表下载股票报告清单到硬盘
def get_stock_report_list(DataFrame, path = '/home/wangshi/script/stocks_reports_list/'):
    # /home/wangshi/script/stocks_reports_list/
    
    # from bs4 import BeautifulSoup
    from math import ceil
    # import requests, urllib, os, shutil, json
    # import pandas as pd
    
    # 总计输出备用
    reports_not_exist_count = 'Reports_Not_Exist:' + '\n'
    
    # 第一层循环，遍历列表中每个股票代码，取得其报告页数
    for stock_code in list(DataFrame['证券代码']):
           
        try:
            url_data_0 = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=1&code=' + stock_code
            html_doc_0 = urllib.request.urlopen(url_data_0).read()
            soup_0 = BeautifulSoup(html_doc_0, "lxml")

            # 用 json 处理得到的 json 文本
            jsontext_0 = json.loads(soup_0.text.split('=', 1)[1].replace('[{stats:false}]','"[{stats:false}]"'))
            
            # 向上取整取得报告页数
            if jsontext_0['data'] == '[{stats:false}]':
                reports_not_exist_count += stock_code + '_' + DataFrame['证券名称'].loc[stock_code] + '\n'
                # print(stock_code + '_' + DataFrame['证券名称'].loc[stock_code] + ' Reports Not Exist')
                pass
                
            else:
                page_numbers = ceil(int(jsontext_0['count'])/25)
        
                data_0 = []
        
                # 第二层循环，遍历股票报告页面，取得其报告编码
                for page_number in range(1, page_numbers + 1):
            
                    url_data_1 = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=' + str(page_number) + '&code=' + stock_code
                    html_doc_1 = urllib.request.urlopen(url_data_1).read()
                    soup_1 = BeautifulSoup(html_doc_1, "lxml")
            
                    # 用 json 处理得到的 json 文本
                    jsontext_1 = json.loads(soup_1.text.split('=', 1)[1].replace('[{stats:false}]','"[{stats:false}]"'))
            
                    #合并新的列表
                    data_0 += jsontext_1['data']
        
                #处理取得的编码为DataFrame，并将结果存盘
                data_1 = pd.DataFrame(data_0)
                data_1.index = data_1['infoCode']
                data_1.index.name = 'infoCodes' # 为避免名称重复这里设置为 infoCodes
            
                # 识别旧数据是否存在
                if os.path.isfile(path + stock_code) == True:
                    data_old = pd.read_csv(path + stock_code, index_col = 'infoCodes')
                    data_delta = df_diff(data_1, data_old)
    
                else:
                    data_delta = data_1
               
                get_eastmoney_stock_report(data_delta, DataFrame['文件夹'].loc[stock_code], DataFrame['证券代码'].loc[stock_code], DataFrame['证券名称'].loc[stock_code])
            
                data_1.to_csv(path + stock_code)
        
        except:
            traceback.print_exc()
            print('Fail to get reports of ' + DataFrame['证券代码'].loc[stock_code] + '_' + DataFrame['证券名称'].loc[stock_code])
            
    # 输出空值文件
    print(reports_not_exist_count + '\n')
    return

industry_codes = ['801120', '801150']

for i in industry_codes:
    temp_list = get_sw_industry_list(i)
    get_stock_report_list(temp_list)

end_time = datetime.now()

print('\n' + 'USED ' + str((end_time - start_time).seconds) + ' seconds!')
print('\n' + str(datetime.now()))

