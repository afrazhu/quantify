import tushare as ts
from sqlalchemy import create_engine

ts.set_token("0b8f33e64a5558e84bd5b7499d0d0d6417d11d7db5d7ae960889f00e")
pro = ts.pro_api()
list = pro.stock_basic(fields='ts_code,symbol,name,fullname,enname,exchange_id,curr_type,list_date,delist_date,is_hs,list_status')
list.to_json('./share_list.json', orient='records')
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/quantify?charset=utf8')
# list.to_sql('shares_list', engine, if_exists='append')