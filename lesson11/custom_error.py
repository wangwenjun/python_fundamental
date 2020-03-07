class MyError(Exception):

    def __init__(self,message=""):
        self.message=message

    def __str__(self):
        return "MyError"



def fun():
    raise MyError("My test error message")

try:
    fun()
except MyError as e:
    print("MyError",e.message)

print("*"*100)

raise MyError()
