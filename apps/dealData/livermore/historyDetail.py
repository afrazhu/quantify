import pandas as pd
import sys
import json
import time, datetime
import os
import tushare as ts
from function import function

sys.path.append("../../../common/")
from Constant import const
from Utility import utility
from Secret import secret

sys.dont_write_bytecode = True

# key point

keyPoint = const.KEY_TIME + "_" + str(const.KEY_MAX) + "_" + str(const.KEY_MIN) + "_" + const.KEY_PRICE
# trend files path
filePrePath = "../file/livermore/trend/"

with open('./share_list.json', 'r') as f:
    datas = json.load(f)

# startTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
startTime = "2019-01-01"
endTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# code list
for data in datas:
    # ts_code = data.get('ts_code')
    code = data.get('symbol')
    # code trend path
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
    while startTime <= endTime:
        df = ts.get_tick_data(code=code, date=startTime, src='tt', pause=0.1)
        if (df is None):
            print(' empty ' + code + "-" + startTime)
        elif (df.empty):
            print(' empty ' + code + "-" + startTime)
        else:
            print(code + ' | ')
            # path time  price  change  volume   amount type
            # generate trends
            for index, row in df.iterrows():
                nowPrice = float(row["price"])
                nowType = function.geneNowType(preValue, lastValue, nowPrice)
                if nowType:
                    preValue['preType'] = nowType
                    preValue['prePrice'] = nowPrice
                    preData = utility.addTwoDimDict(preData, 'lastValue', nowType, nowPrice)

                    listValue = '{"time":"' + str(row["time"]) + '","price":"' + str(nowPrice) + '"},'
                    typeFile = trendFilePath + nowType + ".txt"
                    with open(typeFile, 'a+') as typeF:
                        typeF.write(listValue)

                    print(nowType)
        startTime = datetime.datetime.strptime(startTime, '%Y-%m-%d')
        startTime = (startTime + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        print(startTime)
    preData['preValue'] = preValue
    startTime = datetime.datetime.strptime(startTime, '%Y-%m-%d')
    preData = utility.addTwoDimDict(preData, 'preValue', "preTime",
                                    (startTime - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
    with open(preDataFile, 'w+') as f:
        json.dump(preData, f)
    time.sleep(1)

sys.exit()
