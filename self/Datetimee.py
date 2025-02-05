import datetime

# date = datetime.date(2025,1,4)
# print(date)

# today = datetime.date.today()
# print(today)

# time = datetime.time(12,30,56)
# print(time)

# now = datetime.datetime.now()
# print(now)

# now1 = now.strftime("%H:%M:%S  %d-%m-%Y")
# print(now1)

target_datetime = datetime.datetime(2026 , 1, 1 ,0,0,0)
current_time = datetime.datetime.now()

if target_datetime < current_time:
    print("Date already Passed")
else:
    print("Date NOT passed")