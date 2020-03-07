def add(x,y):
    """
        This function is used for int type add operation.
    """
    if isinstance(x,int) and isinstance(y,int):
        return x+y
    else:
        raise TypeError("the arguments x and y must be int type in add.")

if __name__=="__main__":

    print(add(1,2))
    print(add("hello",123))


