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
try:
    print(x)
except NameError:
    print("변수가 정의되지 않아 오류가 발생함!!!")
def divide(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        print("0나누기 오류발생!")
    else:
        print(c)
divide(30,0)
divide(20,10)
def get_value(list1,n):
    try:
        result=list1[n]
    except IndexError:
        print("인덱스가 범위를 벗어남!!!!")
        result=-1
    finally:
        return result
data=[10,20,30]
print(get_value(data,3))
print(get_value(data,1))