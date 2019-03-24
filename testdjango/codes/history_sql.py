import tushare as ts
import json
import time
from sqlalchemy import create_engine

with open('/home/code/shares/block/industry.json', 'r') as f:
    datas = json.load(f)

startTime = '2001-01-01'
endTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
engine = create_engine('mysql://root:afra_mysql@127.0.0.1/shares?charset=utf8')
for data in datas:
    code = data.get('code')
    single = ts.get_k_data(code, start=startTime, end=endTime)
    single.to_sql(code+'_history', engine, if_exists='append')


