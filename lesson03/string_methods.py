s="alexwang"
print(s.capitalize())
s="ALEXWANG"
print(s.capitalize())
print("*"*100)

s="ALEXWANG is learning python"
print(s.lower())
print(s.upper())

s1=s.lower()
print(id(s1),id(s),s,s1)
print("*"*100)

print(s.startswith("ALE"),type(s.startswith("ALE")))
print(s.startswith("sdf"))
print(s.endswith("python"),s.endswith("on"))

s2=s.strip("python")
print(s2,s,id(s2),id(s))
s2=s.strip("th")
print(s2,s)

print("*"*100)

s3=s.replace("i","")
print(s3)
print(s.replace("ALEXWANG","Jack"))

f=s.find("python")
print(f,type(f))
print(s.find("xyz"))
