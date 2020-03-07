text=input("please type the string:")
l = int(input("how many characters you wanted to UPPER:"))

first=text[:len(text)-l]
second=text[len(text)-l:]
#print(first)
#print(second)
result=first.lower()+second.upper()
print(result)
