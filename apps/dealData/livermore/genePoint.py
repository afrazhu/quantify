import pandas as pd
import sys
import json
import time
import os
from function import function
sys.path.append("../../../common/")
from Constant import const
from Utility import utility
from Secret import secret
import datetime
from dateutil.relativedelta import relativedelta

sys.dont_write_bytecode = True

# database connect
engine = secret.ENGINE

# get code tables
tableSql = "select `table_name` from information_schema.tables where table_schema=%(database)s  and `table_name` LIKE %(tables)s"
tables = pd.read_sql_query(tableSql, engine, params={'database':'quantify', 'tables':'zode_%'})

startTime = datetime.date.today() - relativedelta(months=+1)
# get code details
datas = {}
rowIndex = 0
for i, index in tables.iterrows():
    # code trend path
    code = index["table_name"][5:]
    print(code)
    # get details
    detailSql = "select * from " + index["table_name"] +" where datetime  >  %(datatime)s order by datetime"
    details = pd.read_sql_query(detailSql, engine, params={'datatime':startTime})
    if details.empty:
        continue
    priceHigh = 0
    priceLow = 0
    total = 0
    num = 0
    data = {}
    # generate trends
    for j, row in details.iterrows():
        total = total + row["high"] + row["low"]
        num = num + 2
        if row["high"] > priceHigh:
            priceHigh = row["high"]
        if priceLow == 0:
            priceLow = row["low"]
        if row["low"] < priceLow:
            priceLow = row["low"]
    avg = round(total/num,2)
    time.sleep(0.01)
    data['code'] = code
    data['high'] = priceHigh
    data['low'] = priceLow
    data['avg'] = avg
    data['range'] = round((priceHigh-avg)/2,2)
    rowIndex = rowIndex + 1
    datas[rowIndex] = data
file = "../file/point/point.txt"
with open(file, 'w+') as f:
    json.dump(datas, f)
sys.exit()
