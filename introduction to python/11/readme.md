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
## 🔥`class`
```python
class Cat:
    kor_name="로키"
    eng_name="rocky"
    age=2
    def sound(self):
        print("야옹~~~")
    def speed(self):
        print("엄청 빠르다")
mycat=Cat()
print("한글이름:",mycat.kor_name)
print("영어이름:",mycat.kor_name)
print("나이:",mycat.kor_name)
mycat.sound()
mycat.speed()
```
## 🔥`Attribute`
```python
class Student:
    pet=[]
    def push_pet(self,x):
        self.pet.append(x)
john=Student()
john.push_pet("고양이")
print(john.pet)
sally=Student()
sally.push_pet("이구아나")
print(sally.pet)
class Student:
    def __init__(self):
        self.pet=[]
    def push_pet(self,x):
        self.pet.append(x)
john=Student()
john.push_pet("고양이")
print(john.pet)
sally=Student()
sally.push_pet("이구아나")
print(sally.pet)
```
## 🔥`Method Overriding`
```python
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
class Student(Person):
    pass
x=Student("('홍길동')")
x.show_name()
a="황희찬","황의조","황인범"
x=Student(a)
x.show_name()
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
x=Student("홍길동",20)
x.show_name()
x.show_age()
class Person:
    def __init__(self,name):
        self.name=name        
    def show_name(self):
        print(self.name)
class Student(Person):
    def show_name(self):
        print("환영합니다!!!")
        print(self.name+"님 반갑습니다.")
x=Student("홍길동")
x.show_name()
class person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.ago)
class Student(Person):
    def __init__(self,name,age):
        super(). __init__(name)
        self.age=age
    def introduction(self):
        print("이름은 %s이고 나이는 %d살 입니다."%(self.name,self.age))
x=Student("홍길동",20)
x.show_name()
x.introduction()
```