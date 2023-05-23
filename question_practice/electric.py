import datetime
class electric_vehicle:
    def __init__(self,brand,name):
        self.brandname = brand
        self.customer_name = name

    def transaction_time(self):
        print(f"transaction_time : {datetime.datetime.now()}")

    def welcome(self):
        print(f"welcome to {self.brandname}")

    def vehicle_details(self):
        print(f"brand : {self.brandname}")
        print(f"name : {self.customer_name}")

class ola(electric_vehicle):
    def __init__(self,brand,name):
        super().__init__(brand, name)

class ather(electric_vehicle):
    def __init__(self,brand,name):
        super().__init__(brand, name)

electric_car1 =ola("ola", "ola s1pro")
electric_car2 =ather("ather", "ather_pro 1")

for electric_vehicle in (electric_car1, electric_car2):
    electric_vehicle.welcome()
    electric_vehicle.vehicle_details()
    electric_vehicle.transaction_time()
