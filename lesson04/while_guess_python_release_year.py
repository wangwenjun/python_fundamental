success=False
while not success:
    inputYear=int(input("please guess(input at console) the python release year:"))
    if inputYear>1991:
        print("The python already released, guess again.")
    elif inputYear<1991:
        print("The python not ready for release at all.")
    else:
        print("you are right.")
        success=True
else:
    print("The user guessed successfully and the while loop condition will not True.")

