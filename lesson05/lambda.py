def fun_iterable(iterable):
    l=[]
    for e in iterable:
        l.append(2*e)
    return l

def fun_iterable3(iterable):
    l=[]
    for e in iterable:
        l.append(3*e)
    return l

print(fun_iterable([1,2,3,4,5]))
print(fun_iterable3([1,2,3,4,5]))



def test():
    pass

def foo(x):
    print(x,type(x))

foo(123)

foo(test)

print("*"*100)
def fun_map(iterable,f):
    l=[]
    for e in iterable:
        l.append(f(e))
    return l

def f1(e):
    return 2*e

def f2(e):
    return 3*e


print(fun_map([1,2,3,4,5],f1))
print(fun_map([1,2,3,4,5],f2))
print("*"*100)
###lambda

print(fun_map([1,2,3,4,5],lambda e:2*e))
print(fun_map([1,2,3,4,5],lambda e:3*e))
print(fun_map([1,2,3,4,5],lambda e:10*e))

#basic lambda
add=lambda x,y:x+y
print(add(10,20),type(add))
print("*"*10)

add=lambda x,y:[
    print(x), 
    print(y) ,
    x+y
]
print(add(10,20)[-1],type(add))


def xyz(x):
    return lambda n:n*x

print(xyz(10),xyz(10)(20))

