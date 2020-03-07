class Person:

    gender=None

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greeting(self,greeting):
        print(f"{greeting} {self.name} your age is {self.age}")

    @classmethod
    def person_factory(cls,name,age):
        print("===========",cls,cls.gender)
        instance=cls(name,age)
        return instance

    def __str__(self):
        return f"{self.name},{self.age},{self.gender}"

    @staticmethod
    def static_method(a,b,c):
        print(a,b,c)


print(Person.__dict__)
p1=Person("alex",100)
p2=Person("Jack",200)
print(p1.__dict__,p2.__dict__)
print(Person.gender,p1.gender,p2.gender)
p1.gender="F"

print(Person.gender,p1.gender,p2.gender)
Person.gender="M"
print(Person.gender,p1.gender,p2.gender)
p3=Person("Alice",1000)
print(Person.gender,p1.gender,p2.gender,p3.gender)
print("*"*100)

print(hasattr(Person,"person_factory"))
print(hasattr(p1,"person_factory"))
p4=Person.person_factory("Amy",10)
print(p4)
print("*"*100)

p5=p4.person_factory("Jenny",1000)
print(p5)
print("*"*100)
print(hasattr(Person,"static_method"))
print(hasattr(p1,"static_method"))
p1.static_method(1,2,3)

