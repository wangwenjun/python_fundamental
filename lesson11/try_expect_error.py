def fun():
   a="Hello"
   print(a)
   print([1,2,3][3])
    
try:
    fun()
except (NameError,TypeError) as e:
    if isinstance(e,NameError):
        print("Name Error:",e)
    elif isinstance(e,TypeError):
        print("type",e)
    else:
        pass
except Exception as e:
    print("Unknown Exception",e)
else:
    print("no error found.")
finally:   
    print("always execution")


