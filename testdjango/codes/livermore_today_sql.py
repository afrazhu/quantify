import tushare as ts
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import json
import time
import sys
from sqlalchemy import create_engine

with open('/home/code/shares/block/industry.json', 'r') as f:
    datas = json.load(f)

startTime = '2001-01-01'
endTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
engine = create_engine('mysql://root:afra_mysql@127.0.0.1/shares?charset=utf8')

for data in datas:
    code = data.get('code')
    singles = ts.get_k_data(code, start=startTime, end=endTime)
    if singles['open'] + singles['close'] == 23.393:
        singles['one_point'] = 1
    elif singles['open'] + singles['close'] == 23.915:
        singles['one_point'] = 2
    else:
        singles['one_point'] = 3
    print(singles)
    sys.exit()
    # for single in singles['date']
    #     print(single)
    #     die()
    # singles.to_sql(code+'_history', engine, if_exists='append')


