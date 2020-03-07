l=[1,2,3,4]
print(l,id(l))

print(l.remove(4))
print(l,id(l))

# ValueError: list.remove(x): x not in list
if 100 in l:
    l.remove(100)

print(l,id(l))

print("*"*100)
l=[1,2,3,4]
print(l.pop())
print(l.pop(1))

print(l,id(l),len(l))

#pop index out of range
#print(l.pop(5))

l=[1,2,3,4]
print(l,id(l),len(l))
del l[2]

print(l,id(l),len(l))
print("*"*100)

l=[1,2,3,4]
print(l,id(l),len(l))
print(l.clear())
print(l,id(l),len(l))

print("*"*100)
l=[1,2,3,4]
print(l,id(l),len(l))
del l[:]
print(l,id(l),len(l))

print("*"*100)
l=[1,2,3,4,3,4,2,2]
print(l.index(2))
#ValueError: 2 is not in list
#print(l.index(2,2,5))


