digits=[1,2,3,4,5]
print(digits,'len:',len(digits))
letters=['a','b','c','d']
print(letters,"len:",len(letters))
mixed=[1,2,3,'a','b',[1,2,3,'a','b','c']]
print(mixed,"len:",len(mixed))
print("*"*100)

lists=[1,2,3,4,5,6]
print(lists[0])
print(lists[4])

print(lists[-1])
#Traceback (most recent call last):
#  File "list-basic.py", line 14, in <module>
#    print(lists[-10])
#IndexError: list index out of range
#print(lists[-10])


#Traceback (most recent call last):
#  File "list-basic.py", line 22, in <module>
#    print(lists[10])
#IndexError: list index out of range

#print(lists[10])


print(lists[0:5])
print(lists[:5])

print(lists[2:len(lists)])
print(lists[2:])


print(lists[-4:])
print(lists[2:-2])

print(lists[:],id(lists),id(lists[:]))
s="HelloWorld"
print(s[:],id(s),id(s[:]))

print("*"*100)
print(lists[:6:2])


l1=[1,2,3]
l2=['a','b','c']
l3=l1+l2
print(l1,l2,l3)
print("*"*100)

l=[1,2,3,4,5]
print(id(l),l)
l[1]=l[1]*10
print(id(l),l)

#Traceback (most recent call last):
#  File "list-basic.py", line 60, in <module>
#    s[1]="x"
#TypeError: 'str' object does not support item assignment
#s="HelloWorld"
#print(id(s),s[1],s)
#s[1]="x"
#print(id(s),s[1],s)


l.append("Alex Wang")
print(id(l),l)

