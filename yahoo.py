# -*- coding: utf-8 -*-
import urllib2
import re,json
import datetime
import sqlite3
import requests
from bs4 import BeautifulSoup
# import execjs
import demjson
from get_data_sina_onesql import insert_data

def get_columes(address):
    url = address
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    colume = soup.thead.get_text().encode('utf-8').split('\n')
    while '' in colume:
        colume.remove('')
    return colume

def get_data(address):
    url = address
    page_data = []
    # try:
    response = requests.get(url,)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html = response.text.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # print html
    ptn = re.compile('\{.*\}', re.DOTALL)
    rslt = ptn.findall(html)
    # print rslt
    # print(type(rslt[0]))
    return  rslt[0]


x = get_data("http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList['yl3d4qagkRhWInMj']/Market_Center.getHQNodeDataNew?page=1&num=4000&sort=per_d&asc=0&node=hs_a")
y = get_data("http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList['_y4HiBuMc6BZKJj9']/Market_Center.getHQNodeDataNew?page=1&num=50&sort=pb&asc=0&node=hs_a")



# print x
# print y
list =(x+",").split("},")
data =[]
for i in range(len(list)-1):
    list[i] = list[i]+"}"
    dic= demjson.decode(list[i])
    print dic
    row ="(\""+dic['code']+"\",\""+dic['name']+"\",\""+str(dic['per'])+"\",\""+str(dic['per_d'])+"\")"
    data.append(row)

# print data
insert_data("Finance","pe",data)






