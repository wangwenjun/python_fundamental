class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def att(self):
        self.address=["sdfsdfds","sdfsdfsdf"]

    def greeting(self,greeting):
        print(f"{greeting} {self.name} your age is {self.age}")



if __name__=="__main__":
    p = Person("Alex",20)
    p.greeting("Hello")
    print(hasattr(Person,"name"),hasattr(Person,"age"),hasattr(Person,"att"),hasattr(Person,"greeting"))
    Person.greeting(p,"Hello")
