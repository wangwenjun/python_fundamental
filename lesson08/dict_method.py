d={
        "Name":"Alex",
        "Age":100,
        "Address":"China"
}

print(d,type(d),id(d))
d["Hello"]="World"
print(d,type(d),id(d))
d["Hello"]="Python"
print(d,type(d),id(d))

d.update({"World":"Programming"})
print(d,type(d),id(d))

d.update({"World":"xxxxxxxx"})
print(d,type(d),id(d))

d.update({"k1":123,"k2":234})
print(d,type(d),id(d))
d.update({"k1":13423,"k2":678234})
print(d,type(d),id(d))

d.clear()
print(d,type(d),id(d))
print("*"*100)
d.update({
        "Name":"Alex",
        "Age":100,
        "Address":"China"
})
print(d,type(d),id(d))
del d["Name"]
print(d,type(d),id(d))
d.update({"Name":"Alex"})

x=d.pop("Name")
print(x,type(x))
print(d,type(d),id(d))
a=d.copy()
print(id(a),id(d),a)
print("*"*100)

x=d.popitem()
print(x,type(x))
print(d,type(d),id(d))
print("*"*100)

l=["m1","m2","m3","m4","m5"]
d1=dict.fromkeys(l,"0%")
print(d1)


print(d1.get("m6","10%"))
print(d1)
x=d1.setdefault("m1")
print(x,d1)
x=d1.setdefault("m10")
print(x,d1)
x=d1.setdefault("m20","60%")
print(x,d1)
