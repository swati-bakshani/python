class vehicle:
    def __init__(self,brandname,modelname):
        self.brand= brandname
        self.model = modelname

    def move(self):
        print("move!")

    def vehicle_properties(self):
        print(self.brand, self.model)

class car(vehicle):
    pass

class plane(vehicle):
    def move(self):
        print("fly!")

class boat(vehicle):
    def move(self):
        print("sail!")

car1 = car("kia", "sonnet")
plane1 = plane("kingfisher", "indiafly")
boat1 = boat("boat1", "boeing1")

for vehicle in (car1,plane1,boat1):
    vehicle.vehicle_properties()
    vehicle.move()

