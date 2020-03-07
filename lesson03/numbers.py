import math

integer=49
negative_integer=-35
print(integer,type(integer),negative_integer,type(negative_integer)) #output: 49 <class 'int'> -35 <class 'int'>
large_integer = 34567898327463893216847532149022563647754227885439016662145553364327889985421
print(large_integer,type(large_integer))# 34567898327463893216847532149022563647754227885439016662145553364327889985421 <class 'int'>
n=3.3333
print(n,type(n)) #3.3333 <class 'float'>
#3.141592653589793 <class 'float'>
print(math.pi,type(math.pi))
# 2.718281828459045 <class 'float'>
print(math.e,type(math.e))

i=130
#130 <class 'int'> 130.0 <class 'float'>
print(i,type(i),float(i),type(float(i)))


x=1/3
#0.3333333333333333 <class 'float'>
print(x,type(x))

b=0b111
#7 <class 'int'>
print(b,type(b))

h=0xf
#15 <class 'int'>
print(h,type(h))

o=0o20
#16 <class 'int'>
print(o,type(o))

#0b111 <class 'str'>
print(bin(7),type(bin(7)))
#0xf <class 'str'>
print(hex(15),type(hex(15)))
#0o20 <class 'str'>
print(oct(16),type(oct(16)))
#0xf 0o17
print(hex(0b1111),oct(0b1111))


