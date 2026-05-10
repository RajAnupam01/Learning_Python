class Animal:
    name = "Lion" # class attribute

    def __init__(self,age):
        self.age = age  # instance attribute

    def show(self):  #instance method
        print(f"How are you,{self.age}")

    @classmethod # class method
    def hello(cls):
        # print(f"How are you brother ,{cls.age}")  #doesn't work
        print("How are you brother")
    
    @staticmethod  #static method
    def static():
        print("Hii")

obj = Animal(12)
# obj.show()
# obj.hello()
# obj.static()

