def get_sw_industry_list(industry_code):
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
    
    return datatemp
