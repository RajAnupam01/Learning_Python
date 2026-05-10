"""
class FactoryMumbai:  #parent class
    a = "I am a method mentioned inside factory"
    def hello(self):
        print("Hello i am a method mentioned inside factory")

class FactoryPune(FactoryMumbai):   #child class
    pass

obj = FactoryMumbai()
print(obj.a)
obj2 = FactoryPune()
print(obj.a)

"""
"""
class Animal:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(f"Hello your name is {self.name}")
        

class Human(Animal):
    pass

person1 = Human("Anupam")
person1.show()

"""
class Animal:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(f"Hello your name is {self.name}")
        

class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Hello your name is {self.name} and {self.age} ") # metod overriding.

person1 = Human("Anupam",24)
person1.show()
animal1 = Animal("lion")
animal1.show()


