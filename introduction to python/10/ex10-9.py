f=open("weather.csv" , "w",  encoding="utf-8")
names=["지점명,일시,평균기온(*C),최저기온(*C),강수량(mm),습도(%)","강릉,12월01일,5.7,10.2,1.9,1.4,51.7","강릉,12월02일,5.6,10.2,1.6,0.7,49.6","강릉,12월03일,5.3,10.1,1.2,0.6,48","강릉,12월04일,5,9.7,0.9,2.5,1.1,48","강릉,12월05일,4.9,9.6,0.8,1.6,48.2","강릉,12월06일,4.8,9.4,0.9,2.2,49.6","강릉,12월07일,4.7,9.3,0.9,2.2,49.8"]
for name in names:
    f.write(name+"\n")
print("파일 쓰기 완료")
f.close
import csv
file_name="weather.csv"
f=open(file_name,"r",encoding="utf-8")
lines=csv.reader(f)
for line in lines:
    print(line)
f.close()
file_name="weather.csv"
f=open(file_name,"r",encoding="utf-8")
lines=csv.reader(f)
header=next(lines)
print(header)
f.close
file_name="weather.csv"
f=open(file_name,"r",encoding="utf-8")
lines=csv.reader(f)
header=next(lines)
for lind in lines:
    if line[1]=="12월07일":
        day=line[1]
        min_temp=line[4]
print("%s최저기온:%s도"%(day,min_temp))
f.close
file_name1="weather.csv"
file_name2="weather2.csv"
f1=open(file_name1,"r",encoding="utf-8")
f2=open(file_name2,"w",encoding="utf-8",newline="")
lines=csv.reader(f1)
wr=csv.writer(f2)
header=next(lines)
for i in range(5):
    line=next(lines)
    wr.writerow(line)
print("파일쓰기 종료!!!")
f1.close()
f2.close()