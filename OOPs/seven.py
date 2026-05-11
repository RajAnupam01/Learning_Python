# abstraction does not exist in python but can be achieve using a library 


from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimater(self):
        pass

    @abstractmethod
    def area(self):
        pass



class Square(abstract):
    def __init__(self,side):
        self.side = side


class Circle(abstract):
    def __init__(self,radius):
        self.radius = radius

    def perimater(self):
        print('I have created.')

    def area(self):
        print("I have created this too")

obj = Circle(7)
obj2 = Square(12)