import time
seconds=time.time()
print(seconds)
tm=time.gmtime(1609068498.7929275)
print(tm)
tm=time.localtime(1609068498.7929275)
print("년:",tm.tm_year)
print("월:",tm.tm_mon)
print("일:",tm.tm_mday)
print("시:",tm.tm_hour)
print("분:",tm.tm_min)
print("초:",tm.tm_sec)
string=time.ctime(1609068498.7929275)
print(string)
string=0
tm=time.localtime(time.time())
string=time.strftime("%Y-%m-%d %I:%M:%S %p",tm)
print(string)
print("시작!")
time.sleep(10)
print("10초 후 나타남!")
def func():
    sum=0
    for i in range(1,1000001):
        sum=sum+i
start=time.time()
func()
end=time.time()
print("소요시간:",end-start)
