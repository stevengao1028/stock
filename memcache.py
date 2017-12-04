# -*- coding: utf-8 -*-
import redis
import sqlite3
import json
def redis_json():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)
    # dic ={"1":"ccc","2":"dddd"}
    # r.hmset("test",dic)
    # r.set('star1','bbbb')
    # keys = r.keys()
    # print keys
    # for i in keys:
    #     print i,r.get(i)
    # print(r.hgetall("test"))
    #
    db_name = "FinanceAnalyze.db"
    table = 'profit'
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # conn.text_factory = str
    excute_sql = 'select * from  '+table +' where year = 2017'
    cursor.execute(excute_sql)
    result = cursor.fetchall()
    index = cursor.description

    print type(index)
    dic ={}
    for i in range(len(result)):
        for y in range(len(index)):
            # print index[y][0]
            dic[index[y][0]] = result[i][y]
            r.hmset("line",dic)
    conn.close()
    search_result = []
    keys = r.keys()
    # print r.hgetall("line")
    for key in keys:
        for x in r.hgetall(key):
            if r.hget(key,"stock_code") == "000158" :
                # print x,r.hget(key,x)
                search_result.append(r.hgetall(key))
    return search_result



