class Factory:

    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"Your Object details are {self.material}, {self.pockets}, {self.zips}") 

    
Reebok = Factory("Leather",3,2)
Campus = Factory("Nylon",3,3)

Reebok.show()



