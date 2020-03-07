a={1,2,3,4}
b={4,5,6,7}
print(a,b)
x=a.union(b)
print(x,a,b)
x=b.union(a)
print(x,a,b)
print("*"*100)
x=a|b
print(x,a,b)

print("*"*100)

x=a.intersection(b)
print(x)
print({1,2,3} & {4,5,6})

x=a.difference(b)
print(x)
x=b.difference(a)
print(x)
x=a - b
print(x)
x=b-a
print(x)

a={1,2,3}
b={3,2,1}
print(a==b)


x=a.issubset(b)
print(x)
x=a.issuperset(b)
print(x)
print({1,2,3}.issubset({1,2,3,4}))
a=set([])
b={1}
print(a,b,type(a),type(b))
print(a.issubset(b))
print(a.issuperset(b))
