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
end=time.localtime(time.time())
print("게임종료 시간:",time.strftime("%I:%M:%S %p",end))
print("random():",random.random())
print("random():",random.random())
print("uniform(1,10):",random.uniform(1,10))
print("uniform(1,10):",random.uniform(1,10))
print("randint(1,6):",random.randint(1,6))
print("randint(1,6):",random.randint(1,6))
print("choice([1,2,3,4,5,6]):",random.choice([1,2,3,4,5,6]))
print("choice([1,2,3,4,5,6]):",random.choice([1,2,3,4,5,6]))
print("choice('python'):",random.choice("python"))
print("choice('python'):",random.choice("python"))
list1=[15,23,4,88,7]
print("원래의 리스트:",list1)
random.shuffle(list1)
print("순서가 변경된 리스트:",list1)

x=["가위","바위","보"]
플레이어1=random.choice(["가위","바위","보"])
플레이어2=random.choice(["가위","바위","보"])
print("나:"+플레이어1)
print("당신:"+플레이어2)
if 플레이어1==플레이어2:
            print("draw")
elif 플레이어1=="가위" and 플레이어2=="바위" or 플레이어1=="바위" and 플레이어2=="보" or 플레이어1=="보" and 플레이어2=="가위":
            print("you win")
else:
            print("I winㅋㅋㅋ")
while True:
    again=input("(계속하려면 y 그만하려면 n)")
    if again=="y":
        플레이어1=random.choice(["가위","바위","보"])
        플레이어2=random.choice(["가위","바위","보"])
        print("나:"+플레이어1)
        print("당신:"+플레이어2)
        if 플레이어1==플레이어2:
            print("draw")
        elif 플레이어1=="가위" and 플레이어2=="바위" or 플레이어1=="바위" and 플레이어2=="보" or 플레이어1=="보" and 플레이어2=="가위":
            print("you win :(")
        else:
            print("I winㅋㅋㅋ")
    elif again=="n" :
        break
    else :
         again=input("(계속하려면 y 그만하려면 n)") 
print("game over")