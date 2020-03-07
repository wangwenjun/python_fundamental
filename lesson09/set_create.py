a=set([1,2,3]) ##use set function and pass the list?
print(a,type(a),len(a))
for item in a:
    print(item)

print("*"*100)

a=set("Hello Python")
print(a,type(a),len(a))

a=set((1,2,3,4,5,1,2,3))
print(a,type(a),len(a)) ## use tuple

l=[1,2,3,4,"a","b",[1,2,3]]
print(type(l),l)
#print(set(l))

t=1,
print(set(t))
print(set((1,)))
#print(set((1,2,3,4,(1,2,3),[1,2,3,4])))


print(set([1,2,3,4,5,(1,2,3,4)]))
