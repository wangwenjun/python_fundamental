class A:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __eq__(self,other):
        return self.name==other.name and self.age==other.age

    def __gt__(self,other):
        return self.age>other.age

    def __ge__(self,other):
        return self.age>=other.age

    def __hash__(self):
        return hash((self.name,self.age))
    
#    def __del__(self):
#        print(id(self)," will be del.")

    def __str__(self):

        return f"name:{self.name},age:{self.age}"

    def __repr__(self):
        return f"class A.{id(self)},name:{self.name},age:{self.age}"


a1=A("Alex",100)
a2=A("Alex",100)
l=[a1,a2]
print(len(l),l)
t=a1,a2
print(len(t),t)
d={
        "a1":a1,
        "a2":a2
}
print(len(d),d)

s=set(l)
print(len(s),type(s),s)
for e in s:
    print(e)

s2={a1,a2}
print(len(s2),type(s2),s2)

print("a1.id:",id(a1),"a2.id:",id(a2))
print(a1==a2,a1 is a2)
print("*"*100)
print([1,2,3]>[4,5,6])
print(a1>a2)
print(a1>=a2)
print("*"*100)

a3=A("Jack",100)
print(a3)
del a3

print(a1,a2)

print("*"*100)

print(l,t,d,s)
print(a1,a2)

