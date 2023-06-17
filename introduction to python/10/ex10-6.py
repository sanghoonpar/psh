f=open("scores.txt" , "w",  encoding="utf-8")
names=["손흥민 97 80 93 97 93","안정환 86 100 93 86 90","김민재 91 88 99 79 92","김영권 86 100 93 89 92","한바다 80 100 95 89 90"]
for name in names:
    f.write(name+"\n")
print("파일 쓰기 완료")
f.close
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
f.close()