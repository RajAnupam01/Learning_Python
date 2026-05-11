#polymorphism , method overriding exist but not overloading.

"""
class Animal:
    def show(self):
        print("Hello I am show function from Animal")

    

class Human(Animal):
    def show(self):
        print("Hello I am show function from Human")

obj = Human()
obj.show()

"""

class Animal:
    def show(self):
        print("I am showing")

class Human:
    def show(self):
        print("hello i am also showing")

obj1 = Animal()
obj2 = Human()

obj1.show()
obj2.show()