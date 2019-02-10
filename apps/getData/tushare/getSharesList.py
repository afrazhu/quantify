import tushare as ts
import os
import sys

sys.path.append("../../../common/")
from Secret import secret

ts.set_token(secret.TOKEN)
pro = ts.pro_api()
list = pro.stock_basic(fields='ts_code,symbol,name,fullname,enname,exchange_id,curr_type,list_date,delist_date,is_hs,list_status')
list.to_json('./share_test.json', orient='records')
engine = secret.ENGINE
# list.to_sql('shares_list', engine, if_exists='append')