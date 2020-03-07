class A:

    def eat(self):
        print(f"{type(self).__name__} eat")

class B:

    def walk(self):
        print(f"{type(self).__name__} walk.")

class C(A,B):
    pass

if __name__=="__main__":
    c=C()
    c.eat()
    c.walk()
