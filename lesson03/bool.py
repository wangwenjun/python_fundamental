t=True
f=False

print(t,f,type(t),type(f))

b1=10<1
print(b1)

b2=len("Hello World")==11

b3=10>=9
b4=10<=20

b5=10!=20
print(b2,b3,b4,b5)

i=10
j=10
print(i==j,i is j)
j=20
print(i!=j,i is not j)

class P:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    #def __eq__(self,other):
    #    print("==============")
    #    return self.name==other.name and self.age==other.age

p1=P("Alex",100)
p2=P("Alex",100)

print(p1==p2,p1 is p2,id(p1),id(p2))
