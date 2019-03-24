import tushare as ts
import json
import time
from sqlalchemy import create_engine

todayTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
single = ts.get_k_data('000026', start='2018-05-25', end='2018-05-25')
engine = create_engine('mysql://root:afra_mysql@127.0.0.1/shares?charset=utf8')
#print(single)
single.to_sql('000026_history', engine, if_exists='append')