import tushare as ts
import time
import socket
socket.setdefaulttimeout(20)
#这个接口获取时容易超时
today = ts.get_today_all()
todayDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
today.to_json('/home/code/shares/today/'+todayDate+'.json',orient='records');

