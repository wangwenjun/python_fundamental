d={
        "Name":"Alex Wang",
        "Age":33
}

print(d,type(d),len(d))
print(d["Name"])
print(d.get("Name"))

#Traceback (most recent call last):
#  File "dict_access.py", line 9, in <module>
#    print(d["Hello"])
#KeyError: 'Hello'
#print(d["Hello"])

if "Name" in d:
    print(d["Name"])

if "Hello" in d:
    print(d["Hello"])
else:
    print("the dictionary not contains key:Hello")

print(d.get("Hello"))
print(d.get("Hello","This is the default value."))

d2={
        "Name":None
}

print(d2["Name"])
print(d2.get("Name"))


d={
        "Name":"Alex Wang",
        "Age":33,
        "Address":"China"
}
print(d,type(d),len(d))

for item in d:
    print(item,type(item))

for key in d.keys():
    print(key,type(key),d[key])

print(d.keys(),type(d.keys()))

for v in d.values():
    print(v,type(v))

for key,value in d.items():
    print(key,"=",value)

print(d.items(),type(d.items()))

for i in d.items():
    print(i,type(i),i[0],"=",i[1])

l=[(1,2,"x"),(2,3,"y"),(4,5,"z")]
for i1,i2,i3 in l:
    print(i1,i2,i3)

print(d,id(d))
d["Hello"]="World"
print(d,id(d))
