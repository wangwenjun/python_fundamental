l=[]
print(l,id(l),len(l))

print("*"*100,"append")
l.append(1)
print(l,id(l),len(l))
print("*"*100,"extend")
l.extend([2,3,4])

print(l,id(l),len(l))
l.extend((1,1,1))
print(l,id(l),len(l))
l.extend("Python")
print(l,id(l),len(l))
l1=[1,2,3]
l2=["df","sdf"]
l3=l1+l2
print(l1,l2,l3,id(l1),id(l2),id(l3))
l1=l1+l2
print(id(l1),id(l2))


print("*"*100,"insert(index,item)")
list=[1,2,3]
print(list,id(list),len(list))
list.insert(3,10)
print(list,id(list),len(list),list[2])
list.insert(2,8)
print(list)
list[-1]=100
print(list)
list.insert(100,1000)
print(list)


