class Person:
    def hello(self):
        print("안녕하세요.")
person1=Person()
person1.hello()
class Person:
    name="김영표"
    def hello(self):
        print(Person.name+"님 안녕하세요.")
person1=Person()
person1.hello()
Person.name="황희찬"
person1.hello()
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
class Members:
    def set_info(self,name):
        self.name=name
    def show_info(self):
        print("이름:",self.name)
member1=Members()
member1.set_info("홍길동")
member1.show_info()
member2=Members()
member2.set_info("안정환")
member2.show_info()
class Members:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print("이름:",self.name)
        print("나이:",self.age)
member1=Members("황의조",18)
member1.show_info()
member2=Members("최종화",32)
member2.show_info()
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
class Members:
    total=0
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        Members.total=Members.total+1
    def show_info(self):
        print("이름:%s,전화번호:%s"%(self.name,self.phone))
m1=Members("홍길동","010-1234-5678")
m2=Members("강동원","010-2345-6789")
m3=Members("신지훈","010-3456-7890")
m1.show_info()
m2.show_info()
m3.show_info()
print("총 회원 수:(\n",str(Members.total)+"명")

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
class python:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
a=["print","func","class","list","for","while","module","dict","tuple"]
x=python(a)
x.show_name()
print("등은 파이썬에 사용됨")
import math
print(math.cos(math.sin(math.pi)*math.cos(math.pi)+math.cos(9078)/math.sin(math.cos(5))*math.cos(math.sin(math.pi))+math.tan(-math.pi)+98877607-math.cos(8))/math.cos(math.cos(math.cos(math.pi)))*math.sin(9.8782663476862)+math.cos(12.2334545676878990))
