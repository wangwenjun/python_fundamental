d={}
print(type(d),d)
d=dict()
print(type(d),d)

print(isinstance(d,dict))
print(isinstance(1,int))
print(isinstance([],list))
print(isinstance((),tuple))
print(isinstance("",str))


d={
        "Hello":"World",
        "python":"Programming"
}
print(d,type(d),len(d))
d=dict(
        Hello="World",
        Python="Programming"
)
print(d,type(d),len(d))

d={
        "Name":"Alex",
        "Age":100,
        "Address":{
            "fisrt line":"sdfsdfs",
            "second line":"sdfsdf"
        },
        "l":[1,2,3,4]
}

print(d,type(d),len(d))

print(type(d["Address"]),type(d["l"]))


