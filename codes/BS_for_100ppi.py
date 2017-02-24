
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen


# In[2]:

html = urlopen('http://www.100ppi.com/monitor/')


# In[3]:

soup = BeautifulSoup(html, "lxml")


# In[4]:

d0 = []
for i in soup.find('table',{"bgcolor":"#c7d8ff"}).findAll('td', {'align':'center','bgcolor':'#fafdff'}):
    d0.append(i.get_text().strip('\n'))


# In[5]:

d1 = []
for i in soup.find('table',{"bgcolor":"#c7d8ff"}).findAll('td', {'class':'w1'}):
    d1.append(i.parent.get_text().strip('\n').split('\n'))


# In[6]:

d2 = pd.DataFrame(d1, columns=d0).dropna()


# In[7]:

d2[d0[2]] = d2[d0[2]].apply(pd.to_numeric)
d2[d0[3]] = d2[d0[3]].apply(pd.to_numeric)
d2[d0[4]] = d2[d0[4]].apply(pd.to_numeric)


# In[8]:

d2['较上周初变化'] = round((d2[d0[2]]/d2[d0[3]] -1 ) * 100, 2)
d2['较上月初变化'] = round((d2[d0[2]]/d2[d0[4]] -1 ) * 100, 2)
d0.append('较上周初变化')
d0.append('较上月初变化')


# In[9]:

# d3 = d2[np.abs(d2['较上周初变化']) > 5].sort(d0[5])
d3 = d2[np.abs(d2['较上周初变化']) > 5].sort_values(by = d0[5])


# In[10]:

d4 = ''


# In[11]:

for i in d3.index:
    d4 = d4 + d3[d0[0]][i] + ' ' * abs(4 - len(d3[d0[0]][i])) + '\t'  + str(d3[d0[2]][i]) +'，\t' + '较上周初\t' + str(d3[d0[5]][i]) + '%\t' + ',' + '较上月初\t' + str(d3[d0[6]][i]) + '%' +'\n'


# In[12]:

d4 = d4 + 'from ' + '生意社商品监测 ' + 'http://www.100ppi.com/monitor/'


# In[13]:

import smtplib
from email.mime.text import MIMEText
from email.header import Header


# In[14]:

subject = '生意社商品信息'
smtpserver = 'smtp.139.com'
username = '13730470137'
password = '11223344'
msg = MIMEText(d4,'plain','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.139.com')
smtp.login(username, password)


# In[15]:

sender = '13730470137@139.com'
receiver = '13731239008@139.com'


# In[16]:

try:
    smtp.sendmail(sender, receiver, msg.as_string())
    print('Send Mail Successful ! 0')
except:
    smtp.sendmail(sender, receiver, msg.as_string())
    print('Send Mail Successful ! 1')
else:
    print('Send Mail Successful ! 2')


# In[17]:

smtp.quit()

