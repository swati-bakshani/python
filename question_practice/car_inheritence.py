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

class kia(car):
    def __init__(self,brand,model,name):
        self.customer_name = name
    def welcome(self):
        print(f"welcome {self.customer_name} to our kia family")
 
class maruti(car):
    pass

car1 = kia("kia", "sonnet", "nikhil")
maruti_car2 = maruti("maruti","vitara")

for vehicles in (car1, maruti_car2):
    vehicles.welcome()
    vehicles.transaction_time()