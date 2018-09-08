import tushare as ts
import json
import time
import pandas as pd
from sqlalchemy import create_engine
# ts.set_token("")
# pro = ts.pro_api()
cons = ts.get_apis()
# test = ts.bar('000026', conn=cons)
with open('./share_list.json', 'r') as f:
    datas = json.load(f)

startTime = '2018-09-01'
endTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/quantify?charset=utf8')
for data in datas:
    # ts_code = data.get('ts_code')
    code = data.get('symbol')
    # df = pro.daily(ts_code=ts_code, start_date=startTime, end_date=endTime)
    df = ts.bar(code, conn=cons, start_date=startTime, end_date=endTime)
    if(df is None):
        print(' empty '+code)
        continue
    elif(df.empty):
        print(' empty ' + code)
        continue
    else:
        df.to_sql('zode_'+code, engine, if_exists='append')
        print(code + ' | ')
        time.sleep(0.01)


