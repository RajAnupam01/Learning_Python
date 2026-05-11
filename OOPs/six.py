#Encapsulation

class Factory:
    a = "pune "   # public
    _b = "Bombay"  # protected , does not exist primarily
    __c= "Delhi"   # private

    def show(self):
        print("Hello i am a pune factory")

    def _show2(self):
        print("Hello i am a Bombay Factory")

    def __show3(self):
        print("Hello i am a Delhi FActory")

obj = Factory()
print(obj.__c)