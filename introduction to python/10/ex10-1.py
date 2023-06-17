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