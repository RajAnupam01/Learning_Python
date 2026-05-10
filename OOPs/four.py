"""
class Animal:
    def __init__(self,name):
        pass

class Human: 
    def __init__(self,name,age):
        pass


class Robots(Animal,Human):  
    name="Charlie"

obj = Robots()
print(obj.name1)
print(obj.name2)
print(obj.name3)

"""
class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(Factory,BhopalFactory):
    def __init__(self, material, zips,color,pockets):
        super().__init__(material, zips,color,pockets)
        self.pockets = pockets


obj = PuneFactory("")