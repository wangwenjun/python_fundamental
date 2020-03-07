class Human:

    gender=None

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def eat(self):
        print(f"{type(self).__name__.lower()} eat.")
        return None

    def walk(self):
        print(f"{type(self).__name__.lower()} walk.")

    
    def __str__(self):
        return f"{self.name},{self.gender},{self.age},{self.address}"

class Man(Human):
    pass

class Woman(Human):
    
    def __init__(self,pregnancy,name,age,address):
        #Human.__init__(self,name,age,address)
        super().__init__(name,age,address)
        self.pregnancy=pregnancy
        self.gender="F"

    def suckle(self):
        if self.pregnancy:
            print(f"{self.name} is suckle.")
        else:
            print(f"{self.name} not pregnancy at all.")


class Boy(Man):
    pass

def test():
    
   # m=Man("Alex",100,"CN")
   # print(m,repr(m))
   # w=Woman("Alice",10,"US")
   # print(w,repr(w))
   # m.eat()
   # m.walk()
   # w.eat()
   # w.walk()

   # b=Boy("Jim",8,"UK")
   # print(b,type(b),repr(b))
   # b.eat()
   # b.walk()

    w=Woman(True,"Jenny",30,"AU")
    print(w)
    w.eat()
    w.walk()
    w.suckle()
    

if __name__=="__main__":
    test()

