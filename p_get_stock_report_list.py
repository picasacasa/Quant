def get_stock_report_list(stock_codes,):
    
    from bs4 import BeautifulSoup
    import requests, urllib, os, shutil, json
    import pandas as pd
    
    data0 = None
    
    for i in stock_codes:
        url_stock = 'http://data.eastmoney.com/report/' + i + '.html'
        url_data = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20PrnJnSby={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=25&p'+ str(page_number) + '&code=' + i
        html_doc = urllib.request.urlopen(url_data).read()
        soup0 = BeautifulSoup(html_doc, "lxml")
        jsontext = json.loads(soup0.text.split('=')[1])
        data0 = pd.DataFrame(jsontext['data'])
        data0.index = data0['infoCode']
        data0.index.name = 'infoCode'
        datat.append(data0)
        
    return datat
