a=10
def add(x,y):
    return a+x+y

def fun(x,y):
    z=100
    print(a)
    return x+y+z

print(add(1,2))
print(fun(1,2))

#Traceback (most recent call last):
#  File "global_local_var.py", line 13, in <module>
#    print(z)
#NameError: name 'z' is not defined
#print(z)

