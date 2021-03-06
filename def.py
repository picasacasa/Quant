# DataFrame 的差
def df_diff(df_a, df_b):
    df_a_b = df_a.loc[df_a.index.difference(df_b.index)]
    return df_a_b


# DataFrame 的并
def df_all(df_a, df_b):
    df_a_b = df_a.loc[df_a.index.difference(df_b.index)]
    df_all = df_a_b.append(df_b)
    return df_all

# 获取网页内容
def get_soup(url):
    from bs4 import BeautifulSoup
    import requests, urllib
    html_doc = urllib.request.urlopen(temp_url).read()
    soup = BeautifulSoup(html_doc, "lxml")
    return soup

# 获取网页json内容
def get_web_json(url,decodes = 'utf-8'):
    import requests, urllib
    html_list = urllib.request.urlopen(url_list).read()
    jsontext = json.loads(html_list.decode('utf-8'))
    return jsontext
    

# 用于解决URL编码中带有中文错误的问题
# 类似 'ascii' codec can't encode characters in position 66-70: ordinal not in range(128)
def chinese_able_url(url):
    from urllib.parse import quote
    import  string
    url = quote(url, safe = string.printable)
    return url


##### itchat #####

# 以备注名获取可使用的用户名
# get_UserName_from_RemarkName
def get_UserName(databash,remarkname):
    username = databash[databash['RemarkName']==remarkname]['UserName'][1]
    return username


##### photo / picture #####
# get Original DateTime from picture
def get_exif_date(location):
    import exifread
    try:
        f = open(location,'rb')
        tabs = exifread.process_file(f)
        f.close()
        return tabs['EXIF DateTimeOriginal'].printable
    except:
        return 'EXIF_MESSAGE_ERROR'
