import time


print(time.gmtime(0))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

# current time
print(time.time())
# 1678418065.312507

# getting current time by passing
# the number of seconds since epoch
curr = time.ctime(1678418065.312507)
print("Current time:", curr)

# importing time module
import time

obj = time.gmtime(1627987508.6496193)

# Convert the time.struct_time
# object to a string of the
# form 'Day Mon Date Hour:Min:Sec Year'
# using time.asctime() method
time_str = time.asctime(obj)
print(time_str)

obj = time.localtime(1627987508.6496193)

# Convert the time.struct_time
# object to a string of the
# form 'Day Mon Date Hour:Min:Sec Year'
# using time.asctime() method
time_str = time.asctime(obj)
print(time_str)