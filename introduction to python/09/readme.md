## 💕 모듈

`module`

---

##### 🔥 9-5(모듈)

> 문자열 안에서의 변수 사용

```dart
    import calc as c
x=c.add(100,10)
print(x)
y=c.sub(100,10)
print(y)
```

##### 🔥 9-17(시간)

> List\<T\> list

```dart
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
```

##### 🔥 9-7(수학)

> Map<T, T> map

```dart
    import math
print("sin(2):",math.sin(2))
print("sin(-2):",math.sin(-2))
print("sin(0):",math.sin(0))
print("sin(pi/2):",math.sin(math.pi/2))
print("cos(2):",math.cos(2))
print("cos(-2):",math.cos(-2))
print("cos(0):",math.cos(0))
print("cos(2*pi):",math.cos(2*math.pi))
print("tan(2):",math.tan(2))
print("tan(-2):",math.tan(-2))
print("tan(0):",math.tan(0))
print("tan(pi/4):",math.tan(math.pi/4))
print("ceil(12.3):",math.ceil(12.3))
print("ceil(12.7):",math.ceil(12.7))
print("ceil(-25.2):",math.ceil(-25.2))
print("ceil(-25.8):",math.ceil(-25.8))
print("floor(12.3):",math.floor(12.3))
print("floor(12.7):",math.floor(12.7))
print("floor(-25.2):",math.floor(-25.2))
print("floor(-25.8):",math.floor(-25.8))
print("round(12.3):",round(12.3))
print("round(12.7):",round(12.7))
print("round(-25.2):",round(-25.2))
print("round(-25.8):",round(-25.8))
print(math.fsum([1,2,3,4,5]))
print(math.fsum([1.7,0.3,1.5,4.5]))
print(math.fsum([10,20,30,40,50]))
print("log(75.3):",math.log(75.3))
print("log(pi):",math.log(math.pi))
print("log10(75.3):",math.log10(75.3))
print("log(pi):",math.log10(math.pi))
print("pow(5,2):",math.pow(5,2))
print("pow(100,-2):",math.pow(100,-2))
print("pow(3,0):",math.pow(3,0))
print("sqrt(25):",math.sqrt(25))
print("sqrt(2):",math.sqrt(2))
print("sqrt(pi):",math.sqrt(math.pi))
```

##### 🔥 9-28(활용)
>Map<T,T>map
```dart
    import time
current_time=time.localtime(time.time())
print("게임 시작 시간:",time.strftime("%I:%M:%S %p",current_time))
import random
player1=random.randint(1,6)
player2=random.randint(1,6)
again="y"
while True:
    if again=="y":
        print("two dices are rolling...")
        time.sleep(2)
        player1=random.randint(1,6)
        player2=random.randint(1,6)
        print("플레이어1:"+str(player1))
        print("플레이어2:"+str(player2))
        if player1>player2:
            print("플레이어1 승")
    
        elif player1==player2:
            print("무승부")
        else :
            print("플레이어2 승")
        print("-"*50)
    else:
        break
    again=input("계속하시겠습니까?(y:예,n:아니오)")
print("게임오버")