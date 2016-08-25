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
