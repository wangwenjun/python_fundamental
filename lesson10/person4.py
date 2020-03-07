class Person:
    
    __address=None

    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __str__(self):
        return f"{self.__name},{self.__age},{self.__address}"

    def func1(self):
        """
            public method func1
        """
        print("public method:",self.__name,self.__age,self.__address)

    def _func2(self):
        """
            protected method func2
        """
        print("protected method:",self.__name,self.__age,self.__address)

    def __func3(self):
        """
            private method func3
        """
        print("private method:",self.__name,self.__age,self.__address)

    @classmethod
    def __class_method(cls):
        print(cls)
        return None

    @classmethod
    def class_method_pub(cls):
        cls.__class_method()

#obj=Person("Alex",100)
#print(obj.address,obj.name,obj.age,Person.address)

