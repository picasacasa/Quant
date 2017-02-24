
# coding: utf-8

# In[42]:


from datetime import datetime
start_time = datetime.now()

print('+--------------------+')
print(datetime.now())
from bs4 import BeautifulSoup
import requests, urllib, os, shutil, json
import pandas as pd


# In[2]:

stock_codes = ['000538',]
page_number = 1


# In[ ]:

def get_stock_report_list(stock_codes, path):
    import math
    for stock_code in stock_codes:
        data_0 = None
        # url_stock = 'http://data.eastmoney.com/report/' + i + '.html'
        # url_data = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p'+ str(page_number) + '&code=' + i
        url_data_0 = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=1&code=' + stock_code
        html_doc_0 = urllib.request.urlopen(url_data).read()
        soup_0 = BeautifulSoup(html_doc, "lxml")
        jsontext_0 = json.loads(soup_0.text.split('=')[1])
        page_numbers = math.ceil(int(jsontext_0['count'])/25)
        
        for page_number in range(1, page_numbers + 1):
            url_data_1 = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p=' + str(j) + '&code=' + stock_code
            html_doc_1 = urllib.request.urlopen(url_data_1).read()
            soup_1 = BeautifulSoup(html_doc_1, "lxml")
            jsontext_1 = json.loads(soup_1.text.split('=')[1])
            data_1 = pd.DataFrame(jsontext_1['data'])
            data_1.index = data_1['infoCode']
            data_1.index.name = 'infoCode'
            data_0.append(data_1)
        data_0.to_csv('/home/wangshi/script/stocks_reports_list/' + i)
    return


# url_stock = 'http://data.eastmoney.com/report/' + stock_code + '.html'
# url_data = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p'+ str(page_number) + '&code=' + str(stock_code)

# In[4]:

url_data


# In[5]:

html_doc = urllib.request.urlopen(url_data).read()


# In[6]:

html_doc


# In[7]:

soup0 = BeautifulSoup(html_doc, "lxml")


# In[8]:

soup0


# In[9]:

soup0.text.split('=')[1]


# In[10]:

jsontext = json.loads(soup0.text.split('=')[1])


# In[11]:

jsontext


# In[12]:

datat = pd.DataFrame(jsontext['data'])


# In[14]:

datat.index = datat['infoCode']
datat.index.name = 'infoCode'


# In[15]:

datat


# In[24]:

def get_eastmoney_stock_report(urls, paths):
    # 下载个股
    from dateutil.parser import parse
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
            temp_name = paths + parse(urls.loc[urls.index[i]]['datetime']).strftime('%Y'+'%m'+'%d') + '_' + urls.loc[urls.index[i]]['insName'] + '_' + urls.loc[urls.index[i]]['title'] + '.pdf'
        
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


# In[41]:

get_eastmoney_report(datat, '/home/wangshi/')


# In[26]:

from dateutil.parser import parse


# In[28]:

count_download = 0
count_pass = 0
count_fail = 0


# In[31]:

html_doc = urllib.request.urlopen('http://data.eastmoney.com/report/20160506/APPH3krGmemfASearchReport.html').read()
soup = BeautifulSoup(html_doc, "lxml")


# In[32]:

file_url = soup.find_all(text = '查看PDF原文')[0].parent.get('href')
temp_name = paths + parse(datat.loc[datat.index[i]]['datetime']).strftime('%Y'+'%m'+'%d') + '_' + datat.loc[datat.index[i]]['insName'] + '_' + datat.datat[datat.index[i]]['title'] + '.pdf'


# In[33]:

file_url


# In[34]:

if os.path.isfile(temp_name) == True:
    count_pass += 1
    pass
else:
    urllib.request.urlretrieve(file_url, temp_name)
    count_download += 1


# In[39]:

temp_name = parse(datat.loc[datat.index[i]]['datetime']).strftime('%Y'+'%m'+'%d') + '_' + datat.loc[datat.index[i]]['insName'] + '_' + datat.loc[datat.index[i]]['title'] + '.pdf'


# In[40]:

temp_name


# In[ ]:



