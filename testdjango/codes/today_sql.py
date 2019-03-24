import tushare as ts
import socket
from sqlalchemy import create_engine

socket.setdefaulttimeout(10000)
today = ts.get_today_all()
#print(today)
engine = create_engine('mysql://root:afra_mysql@127.0.0.1/shares?charset=utf8')
today.to_sql('shares_today',engine,if_exists='append')
