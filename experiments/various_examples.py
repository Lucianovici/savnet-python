import os
import platform
from datetime import date, datetime, time, timedelta
import time as ttt

print(platform.platform())
print(os.name)

print(os.listdir('/Users/lucian/Projects'))

os.system("mkdir /tmp/ceva-dubios")
print(os.listdir("/tmp"))
print(os.getcwd())

print(date.today())
now = datetime.now()
a_year_ago_date = now.replace(year=2023)
print(a_year_ago_date)

print(a_year_ago_date.weekday())

print(time(17, 42, 10, 5))

print(ttt.gmtime())

birth_date = datetime(2000, 6, 2, 2, 10, 10)
conception_date = birth_date - timedelta(days=30 * 9)
print(conception_date)

start_date = datetime(2001, 1, 1, 1, 1)
end_date = datetime(2011, 10, 4, 3, 1)

diff_timedelta = end_date - start_date
print(f'Total number of seconds between the dates: {diff_timedelta.total_seconds()}')
