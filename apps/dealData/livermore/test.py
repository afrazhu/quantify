import datetime,time
from dateutil.relativedelta import relativedelta

# startTime = '2019-01-01'
# str2date = datetime.datetime.strptime(startTime, '%Y-%m-%d')
# print(str2date.strftime('%Y-%m-%d'))
# print((str2date + datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
# print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
startTime = "2019-01-01"
startTime = datetime.datetime.strptime(startTime, '%Y-%m-%d')
startTime = (startTime + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
print(startTime)
