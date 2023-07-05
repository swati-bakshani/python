# welcome nikhil to kia
# car: model, brand

import datetime
class car:
    def __init__(self,brandname,modelname):
        self.brand = brandname
        self.model = modelname
    def transaction_time(self):
        print(f"transaction_time : {datetime.datetime.now()}")

    def welcome(self):
        print(f"welcome to our car family")

    def get_car_details(self):
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")

class kia(car):
    def __init__(self,brand,model,name):
        super().__init__(brand, model)
        self.customer_name = name
    def welcome(self):
        print(f"welcome {self.customer_name} to our kia family")

class maruti(car):
    pass

class honda(car):
    def __init__(self,brand,model,name):
        super().__init__(brand,model)
        self.customer_name = name

    def welcome(self):
        print(f"welcome {self.customer_name} to the world of honda")


car1 = kia("kia", "sonnet", "nikhil")
maruti_car2 = maruti("maruti","vitara")
honda_car2 = honda("honda", "honda_city","swati")


for vehicles in (car1, maruti_car2,honda_car2):
    vehicles.welcome()
    vehicles.transaction_time()
    vehicles.get_car_details()