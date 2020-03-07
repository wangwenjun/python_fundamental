a=set([1,2,3,4,5])
print(a,type(a),len(a),id(a))
x=a.add(6)
print(x)
print(a,type(a),len(a),id(a))
x=a.add(6)
print(x)
print("*"*100)
x=a.update({1,2,3,4,5,6,7,8,9})
print(x)
print(a,type(a),len(a),id(a))
a={1,2,3,4,5,6}

print(a,type(a),len(a),id(a))
a.update([1,2,3,4,10])
print(a,type(a),len(a),id(a))
#Traceback (most recent call last):
#  File "set_methods.py", line 17, in <module>
#    print(a[1])
#TypeError: 'set' object does not support indexing
#print(a[1])


x=a.pop()
print(x)
print(a,type(a),len(a),id(a))
a={1}
print(a.pop())
#Traceback (most recent call last):
#  File "set_methods.py", line 29, in <module>
#    print(a.pop())
#KeyError: 'pop from an empty set'
#print(a.pop())

a=set([1,2,3,4,5])
print(a,type(a),len(a),id(a))

x=a.remove(1)
print(x)
print(a,type(a),len(a),id(a))

#Traceback (most recent call last):
#  File "set_methods.py", line 43, in <module>
#    x=a.remove(10)
#KeyError: 10
#x=a.remove(10)
#print(a,type(a),len(a),id(a))

x=a.discard(10)
print(x)
print(a,type(a),len(a),id(a))
x=a.discard(2)
print(x)
print(a,type(a),len(a),id(a))

a.clear()
print(a,type(a),len(a),id(a))


a={1,2,3,4,5}
print(1 in a)
print(10 in a)

