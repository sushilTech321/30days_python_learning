# class polymorphism 

class Car :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move")
        
class Boat: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane: 
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("fly")

c = Car("Ford","Mustang")
b = Boat("Local","dunga")
p = Plane("Hawai","Jahaj")

# c.move()
# b.move()
# p.move()

for x in (c,b,p):
    # print(x.model)
    # print(x.brand)
    # print(x)
    x.move()



