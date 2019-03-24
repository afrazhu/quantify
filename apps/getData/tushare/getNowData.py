import tushare as ts
import os

df = ts.get_realtime_quotes('000581')
print(df)
cmd = '/usr/bin/osascript -e "display notification \\" 提醒内容 \\" with title \\"提醒标题\\""'
print(cmd)
os.system(cmd)
