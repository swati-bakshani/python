import datetime

class electric_car:
    def __init__(self,brand_name,model_name):
        self.brand = brand_name
        self.model = model_name

    def welcome(self):
        print("welcome to our car family")

    def transaction_time(self):
        print(f"transaction time is : {datetime.datetime.now()}")

    def car_details(self):
        print(f"Brand name : {self.brand} , Model Name : {self.model}")

class kia(electric_car):
    def __init__(self,brand_name,model_name,name):
        super().__init__(brand_name,model_name)
        self.customer_name = name
    def welcome(self):
        print(f"welcome {self.customer_name} to our kia family")

class maruti(electric_car):
    pass

class honda(electric_car):
    def __init__(self, brand_name, model_name, name):
        super().__init__(brand_name, model_name)
        self.customer_name = name

    def welcome(self):
        print(f"welcome {self.customer_name} to our honda family")

car_kia = kia("kia","sonet","nikhil")
car_maruti = maruti("maruti","swift")
car_honda = honda("honda","honda_city","chitresh")

for car in (car_kia,car_maruti,car_honda):
    car.welcome()
    car.car_details()
    car.transaction_time()



