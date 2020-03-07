def add(x,y):
    return x+y


print(add(1,3))
print(add(y=100,x=20))


def sum(x,y=10):
    return x+y

print(sum(10))
print(sum(10,20))
print(sum(y=200,x=3))

"""
    def var_sum(args:Int*):Int={
    
    
    }

    private int var_sum(int ... args)
    {
        
    }

"""
def var_sum(*args):
    total=0
    for e in args:
        total+=e
    return total

print(var_sum(1,2,3,4,5,6,7))

print(var_sum())

def var_test(x,*y):
    print(x)
    print(y)

var_test(1,2,3,4,5)
