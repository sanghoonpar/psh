import datetime
time1=datetime.timedelta(days=3,hours=3,minutes=30)
time2=datetime.timedelta(days=5,hours=5,minutes=40)
print(time2-time1)
today=datetime.date.today()
print(today)
today=datetime.date.today()
week=datetime.timedelta(weeks=1)
next_week=today+week
print("오늘:",today)
print("일주일 후:",next_week)
