i=1
while i<10:
    j=1
    while j<=i:
        print(i,"*",j,"=",i*j,end="")
        if i!=j:
            print(", ",end="")
        else:
            pass
        j+=1
    print()
    i+=1
