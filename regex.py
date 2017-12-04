import re
import sqlite3
# letters =[ "580%~600%","-10%~10%","20"]
# for letter in letters:
#     low   = ""
#     high  = ""
#     list = letter.split("~")
#     print len(list),
#     low =list[0]
#     if len(list) > 1:
#         high = list[1]
#     # print type(low)
#     print float(low.split("%")[0]),
#     print high.split("%")[0]


def percent_float(text):
    list = text.split("~")
    if len(list) > 1:
        up = list[1].split("%")[0]
    else:
        up =  ""
    low = list[0].split("%")[0]
    dic ={"lower":low,"upper":up}
    return dic


