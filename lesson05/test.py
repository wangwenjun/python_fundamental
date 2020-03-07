import test2

print("Hello i am the test")
print(__name__)


def add(a,b):
    print("The add function executed")
    return a+b


if __name__=="__main__":
    result=add(10,20)
    print("The result is:",result)

