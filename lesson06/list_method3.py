l=[1,2,3,4,5,6,7,2,2]
print(l.count(2))
print(l.count(100))

if l.count(100)!=0:
    l.remove(100)
else:
    l.append(100)

print(l)

l=[546,234,456,2,3,28,-10]
print(l)
l.sort()
print(l)
l.sort(reverse=True)

print("*"*100)

l=[[1,2],[34,34],[-10,20]]
print(l)
l.sort()
print(l)


def s(li):
    return li[1]

print("*"*100)
l=[["Jack",30],["Lucy",28],["Alice",55]]
print(l)
#l.sort(key=s)
l.sort(key=lambda li:li[1])
print(l)

print("%"*100)
l=[34,34,2,78,45,34,23]
print(l)
l.reverse()
print(l)


print("%"*100)
l=[1,2,3,4,5]
print(l,id(l))
l2=l.copy()
print(l2,id(l2))
print(l==l2,l is l2)
print("#"*100)

l1=[1,2]
l2=[3,4]
lx=[l1,l2]
ly=lx.copy()
print(lx,ly,id(lx),id(ly),id(lx[0]),id(ly[0]))

lx[0].append(100)
print(lx,ly)


