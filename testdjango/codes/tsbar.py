import tushare as ts
cons = ts.get_apis()
test = ts.bar('000026', conn=cons)
#依然是历史数据
print(test)