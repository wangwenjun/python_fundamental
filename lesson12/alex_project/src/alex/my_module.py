class Person:
    """
        This is a simple class Person
    """

    def __init__(self,name,age=10,address="CN"):
        """
            the Person class construct method.
        """
        self.name=name
        self.age=age
        self.address=address

    @classmethod
    def create_person(cls,name,age,address):
        """
            the factory method used create Person instance
        """
        instance=cls(name,age,address)
        return instance


    def __str__(self):
        """
           override the __str__ method 
        """
        return f"name:{self.name},age:{self.age},address:{self.address}"


    def __hash__(self):
        """
            override the hash method used for set data struction
        """
        return hash((self.name,self.age,self.address))


    def simple_function(self):
        """
            simple function in Person class.
        """
        pass


l=[1,2,3,4]
d={}
t=1,2,3
s=set(l)


def fun():
    """
        this is the module function fun(), very simple
        do nothing.
    """
    pass
