f=open("NEW_FILE.txt" , "w",  encoding="utf-8")
names=["홍지수","안지영","김연수","김예린","한정연"]
for name in names:
    f.write(name+"\n")
print("파일 쓰기 완료")
f.close
f=open("NEW_FILE.txt","a",encoding="utf-8")
names=["손영민","황현준"]
for  name in names:
    f.write(name+"\n")
f.close
f=open("NEW_FILE.txt","r",encoding="utf-8")
lines=f.readlines()
print(lines)
f.close
f=open("NEW_FILE.txt","r",encoding="utf-8")
lines=f.readlines()
for line in lines:
    temp=line.replace("\n","")
    print(temp)
f.close
with open("NEW_FILE.txt","r",encoding="utf-8")as f:
    for line in f:
        temp=line.replace("\n"," ")
        print(temp)
f=open("scores.txt","r",encoding="utf-8")
lines=f.readlines()
for line in lines:
    data=line.split()
    i=0
    sum=0
    while i<len(data):
        if i==0:
            print(data[i],end=":")
        else:
            sum=sum+int(data[i])
        i=i+1
    avg=sum/(len(data)-1)
    print("%.2f점"%(sum/5))
f.close