import tushare as ts
from sqlalchemy import create_engine
share_list = ts.get_stock_basics()
#share_list.to_json('/home/code/shares/block/share_list.json',orient='records');
engine = create_engine('mysql://root:afra_mysql@127.0.0.1/shares?charset=utf8')
share_list.to_sql('shares_list',engine,if_exists='append')

