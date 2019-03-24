import tushare as ts
import json
import time
#f = open('/home/code/shares/block/industry.json', "r")
#content = f.read()
#f.close()
with open('/home/code/shares/block/industry.json', 'r') as f:
    datas = json.load(f)

startTime = '2001-01-01'
endTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
for data in datas:
    code = data.get('code')
    single = ts.get_k_data(code,start=startTime,end=endTime)
    single.to_json('/home/code/shares/history/'+code+'.json',orient='records');
    print(code+' | ')

