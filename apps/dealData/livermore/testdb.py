import pymysql
import sys
import os
import pandas as pd

sys.path.append("../../../common/")
from Secret import secret

conn = pymysql.connect(host=secret.DB_HOST,
                       port=secret.DB_PORT,
                       user=secret.DB_USER,
                       passwd=secret.DB_PWD,
                       db=secret.DB_NAME)
cur = conn.cursor()

tableSql = "select `table_name` from information_schema.tables"
cur.execute(tableSql)
results = cur.fetchall()
# print(results)
cur.close()

engine = secret.ENGINE
tables = pd.read_sql_query(tableSql, engine)
# print(tables)
