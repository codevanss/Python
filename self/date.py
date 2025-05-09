import datetime


target_datetime = datetime.datetime(2026 , 1, 1 ,0,0,0)
current_time = datetime.datetime.now()

if target_datetime < current_time:
    print("Date already Passed")
else:
    print("Date NOT passed")