class vehicle:
    def __init__(self,brand_name,model_name,owner_name):
        self.brand = brand_name
        self.model = model_name
        self.name = owner_name

    def vehicle_details(self):
        print(self.brand,self.model)

    def move(self):
        print("move!")

    def message(self):
        print(f"The vehicle is of mr {self.name}"+ " prospering business_man")
        print(f"The vehicle is of mr Nikhil" + " prospering business_man")
class car(vehicle):
    pass
class plane(vehicle):
    def move(self):
        print("fly!")

class boat(vehicle):
    def move(self):
        print("sail!")

car = car("kia","sonnet","nikhil")
plane = plane("indigo","flying_machine","swati")
boat = boat("vikrant","boeing_47", "vikas")

for transport in (car,plane,boat):
    transport.vehicle_details()
    transport.move()
    transport.message()






