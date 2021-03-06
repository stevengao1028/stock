# -*- coding: utf-8 -*-
import urllib2
import re
import datetime
import sqlite3
import requests
from bs4 import BeautifulSoup
import multiprocessing
from DBUtils.PooledDB import PooledDB
import MySQLdb

# pool = PooledDB(MySQLdb,5,host='localhost',user='root',passwd='pwd',db='test',port=3306)

# create db
def create_db(db,address):
    db_name = db
    url = address
    # print url
    for each_url in url:
        add_table(db_name, each_url)
        insert_columes = get_columes(url[each_url])
        add_columes(db_name, each_url,insert_columes)

#add table
def add_table(db,table):
    db_name = db+".db"
    table_name = table
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    conn.text_factory = str
    create_table_sql = 'create table IF NOT EXISTS '+table_name+'  (year varchar(20),quarter varchar(20))'
    try:
        cursor.execute(create_table_sql)
        result = "sucessful"
    except:
        result = table_name+" created fault"
    finally:
        conn.close()
        return result

#columes must be  list
def add_columes(db,table,columes):
    db_name = db + ".db"
    table_name = table
    alert_colume = columes
    # print type(alert_colume)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    conn.text_factory = str
    result = ""
    for each_colume in alert_colume:
        # print each_colume
        add_columes_sql = 'ALTER  TABLE ' + table_name + ' ADD COLUMN  "'+each_colume+'" varchar(50)'
        print add_columes_sql
        try:
            cursor.execute(add_columes_sql)
            conn.commit()
            result = "sucessful"
        except:
            result = alert_colume[each_colume] + ","
    if result != "sucessful":
        result = result.rstrip(',') + " add fault"
    return result

#page_data must be a list
def insert_data(db,table,page_data):
    db_name = db + ".db"
    table_name = table
    insert_data = page_data
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    conn.text_factory = str
    insert_data_sql = 'INSERT INTO '+table_name+' VALUES '+ ",".join(insert_data)
    # print insert_data_sql
    result = ""
    try:
        cursor.execute(insert_data_sql)
        conn.commit()
        result = "sucessful"
    except:
        db.rollback()
        result = "data insert fault"
    finally:
        conn.close()
        return result


#term must be list
def search_data(db, table, term):
    db_name = db + ".db"
    table_name = table
    search_term = term
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    conn.text_factory = str
    search_data_sql = ' SELECT * FROM ' + table_name + ' where '
    for each_term in search_term:
        search_data_sql = search_data_sql+each_term+search_term[each_term]+" and "
    search_data_sql =search_data_sql[:-4]
    # print search_data_sql
    try:
        cursor.execute(search_data_sql)
        result = cursor.fetchall()
    except :
        result = "no result or condition error"
    finally:
        conn.close()
        return result

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


def get_data(address,year,quater,page):
    url = address
    year = year
    quater = quater
    page_num = page
    # try:
    #response = requests.get(url,params={'reportdate':year,'quarter':quater,'p':page_num})
    response = requests.get(url,params={'reportdate':year,'quarter':quater,'p':page_num})
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.get_text())
    page_data = []
    tr_context = soup.find_all('tr')
    for tr in tr_context:
        line_tostr = []
        line = tr.get_text().encode('utf-8').split('\n')
        while '' in line:
            line.remove('')
        line.insert(0, quater)
        line.insert(0, year)
        for i in line:
            line_tostr.append('"'+i+'"')
        # print "("+",".join(line_tostr)+")"
        page_data.append("("+",".join(line_tostr)+")")
    # colume = page_data[0].lstrip('(').rstrip(')').split(',')
    # del colume[0]
    # del colume[0]
    del page_data[0]
    return  page_data


# FinanceAnalyze web address
db_name = "FinanceAnalyze"
fi_url_sina = {}
fi_url_sina['profit'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml'
fi_url_sina['operation'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/operation/index.phtml'
fi_url_sina['grow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/grow/index.phtml'
fi_url_sina['debtpaying'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/debtpaying/index.phtml'
fi_url_sina['cashflow'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/cashflow/index.phtml'
fi_url_sina['main'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml'
fi_url_sina['performance'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml'
# fi_url_sina['news'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/news/index.phtml'
# fi_url_sina['incomedetail'] = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/incomedetail/index.phtml'




#excute
# create_db(db_name,fi_url_sina)
#
# start_year = 1990
# end_year = 2017
# frist_quarter = 1
# end_quarter = 4
# for each_table in fi_url_sina:
#     address = fi_url_sina[each_table]
#     table = each_table
#     while start_year <= end_year:
#         start_quarter = frist_quarter
#         while start_quarter <= end_quarter:
#             for page in range(1, 100):
#                 # print address
#                 # print "year:",start_year,"quarter:",start_quarter,"page:",page
#                 result = get_data(address,str(start_year),str(start_quarter),str(page))
#                 # for i in result:
#                 #     print i
#                 insert_data(db_name, table, result)
#             start_quarter = start_quarter + 1
#         start_year = start_year + 1


def excute_1(table):
    start_year = 2013
    end_year = 2017
    frist_quarter = 1
    end_quarter = 4
    address = fi_url_sina[table]
    table = table
    while start_year <= end_year:
        start_quarter = frist_quarter
        while start_quarter <= end_quarter:
            for page in range(1, 100):
                # print address
                result = get_data(address, str(start_year), str(start_quarter), str(page))
                if result:
                    # print address
                    print table, " year:", start_year, "quarter:", start_quarter, "page:", page
                    insert_data(db_name, table, result)
                else:
                    print "no data",table , "   ",start_year,"     ", start_quarter,"     ", page
                    break
            start_quarter = start_quarter + 1
        start_year = start_year + 1


if __name__ == "__main__":
    # create_db(db_name, fi_url_sina)
    p1 = multiprocessing.Process(target = excute_1, args = ("profit",))
    # p2 = multiprocessing.Process(target = excute_1, args = ("operation",))
    # p3 = multiprocessing.Process(target = excute_1, args = ("grow",))
    # p4 = multiprocessing.Process(target = excute_1, args= ("debtpaying",))
    # p5 = multiprocessing.Process(target = excute_1, args= ("cashflow",))
    # p6 = multiprocessing.Process(target = excute_1, args= ("main",))
    # p7 = multiprocessing.Process(target = excute_1, args= ("performance",))

    p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p6.start()
    # p7.start()
