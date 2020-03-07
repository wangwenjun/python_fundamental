"""
    caculate the sum of iteration type
"""
def sum(the_list_of_numberic):
    count=0
    for e in the_list_of_numberic:
        count+=e
    return count


print(sum)
print(type(sum))

result=sum(range(11))
print(type(result),result)


l=[1,2,3,4,5,6,7,8,9,10]

result=sum(l)
print(type(result),result)


#l=["H","e","l","l","o"]
#result=sum(l)
#print(type(result),result)



def join(a,b):
    return a+b


print(join(1,2),type(join(1,2)))
print(join("x","y"),type(join("x","y")))


def fun(x,y):
    s=x+y

print(fun(1,2))
