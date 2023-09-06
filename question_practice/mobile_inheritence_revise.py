import datetime

class Mobile:
    def __init__(self,brand,model):
        self.brandname = brand
        self.modelname = model

    def mobile_name(self):
        print(f"(brand : {self.brandname}")
        print(f"(model : {self.modelname}")

    def print_year(self):
        print(f"(year : self.year)")

    def transaction_date(self):
        print(f"(transaction time : {datetime.datetime.now()})")

class Samsung(Mobile):
    def __init__(self,brand,model):
        super().__init__(brand,model)
        self.year = 2020

    def welcome(self):
        print("welcome to samsung")

class Oppo(Mobile):
    def __init__(self,brand,model):
        super().__init__(brand,model)
        self.year = 2023

    def welcome(self):
        print("welcome to oppo")

s1 = Samsung("samsung","s20+")
o1 = Oppo("oppo", "o20")

for mobile in (s1,o1):
    mobile.mobile_name()
    mobile.print_year()
    mobile.transaction_date()
    mobile.welcome()



