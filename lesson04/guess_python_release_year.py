ACTUALLY_RELEASE_YEAR=1991
inputYear=int(input("please guess(input at console) the python release year:"))

if inputYear>ACTUALLY_RELEASE_YEAR:
    print("maybe the release year is old than your guess",inputYear)
elif inputYear<ACTUALLY_RELEASE_YEAR:
    print("oh, python not ready for release at all in ",inputYear)
else:
    print("You are smart. that the right!")
