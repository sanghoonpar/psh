## 오늘 학습한 내용

#### `module`, `time`,`math`

## 🔥`txt.`

```python
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
```

## 🔥`csv`
```python
import csv
file_name="weather.csv"
f=open(file_name,"r",encoding="utf-8")
lines=csv.reader(f)
for line in lines:
    print(line)
f.close()
```
## 🔥`json`
```python
import json
member={
    "id":"swhong",
    "name":"홍성우",
    "age":23,
    "history":[
        {"date":"2021-03-15","route":"mobile"},
        {"date":"2020-06-23","route":"pc"}
    ]
}
json_string=json.dumps(member,ensure_ascii=False,indent=4)
print(json_string)
member={
    "id":"swhong",
    "name":"홍성우",
    "age":23,
    "history":[
        {"date":"2021-03-15","route":"mobile"},
        {"date":"2020-06-23","route":"pc"}
    ]
}
with open("member.json","w",encoding="utf-8")as f:
    json.dump(member,f,ensure_ascii=False,indent=4)
with open("member.json","r",encoding="utf-8")as f:
    dict=json.load(f)
    print(dict)
```


