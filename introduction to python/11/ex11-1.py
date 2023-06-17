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