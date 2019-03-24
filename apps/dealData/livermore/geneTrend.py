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

sys.dont_write_bytecode = True

# database connect
engine = secret.ENGINE

# key point

keyPoint = const.KEY_TIME + "_" + str(const.KEY_MAX) + "_" + str(const.KEY_MIN) + "_" + const.KEY_PRICE
# trend files path
filePrePath = "../file/livermore/trend/"

# get code tables
tableSql = "select `table_name` from information_schema.tables where table_schema=%(database)s  and `table_name` LIKE %(tables)s"
tables = pd.read_sql_query(tableSql, engine, params={'database':'quantify', 'tables':'zode_%'})

# get code details
for i, index in tables.iterrows():
    # code trend
    code = index["table_name"][5:]
    trendFilePath = filePrePath + code + "/" + keyPoint + "/"
    utility.mkdir(trendFilePath)
    # get preData (type:dict)
    preDataFile = trendFilePath + const.PRE_VALUE_FILE
    preData = function.getPreValue(preDataFile)
    if preData:
        preValue = preData.get("preValue")
        lastValue = preData.get("lastValue")
        startTime = preValue.get("preTime")
    else:
        preValue = {}
        lastValue = {}
        startTime = const.KEY_TIME
    # get details
    detailSql = "select * from " + index["table_name"] +" where datetime  >  %(datatime)s order by datetime"
    details = pd.read_sql_query(detailSql, engine, params={'datatime':startTime})
    if details.empty:
        continue

    # generate trends
    for j, row in details.iterrows():
        nowPrice = float(row[const.KEY_PRICE])
        nowType = function.geneNowType(preValue, lastValue, nowPrice)
        if nowType:
            preValue['preType'] = nowType
            preValue['prePrice'] = nowPrice
            preData = utility.addTwoDimDict(preData, 'lastValue', nowType, nowPrice)

            listValue = '{"time":"' + str(row["datetime"]) + '","price":"' + str(nowPrice)+'"},'
            typeFile = trendFilePath + nowType + ".txt"
            with open(typeFile, 'a+') as typeF:
                typeF.write(listValue)

            print(nowType)

    preData['preValue'] = preValue
    preData = utility.addTwoDimDict(preData, 'preValue', "preTime", str(row["datetime"]))
    with open(preDataFile, 'w+') as f:
        json.dump(preData, f)

    time.sleep(0.01)

sys.exit()
