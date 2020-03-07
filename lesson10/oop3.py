class Human:

    def __init__(self,name):
        self.name=name

class Father(Human):

    def __init__(self,name,gender):
        Human.__init__(self,name)
        self.gender=gender

    def eat(self):
        print("father eat.")

class Mother(Human):

    def __init__(self,name,address):
        Human.__init__(self,name)
        self.address=address

    def eat(self):
        print("mother eat.")

class Child(Mother,Father):
    
    def __init__(self,name,gender,address,age):
        Father.__init__(self,name,gender)
        Mother.__init__(self,name,address)
        self.age=age

    def eat(self):
        Father.eat(self)


def test():
    f=Father("Alex","M")
    print(f,type(f))

    m=Mother("Alice","HK")
    print(m,type(m))
    c=Child("Jack","M","UK",100)
    print(c,type(c),c.__dict__)

    c.eat()

if __name__=="__main__":
    test()

