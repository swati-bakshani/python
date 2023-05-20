# inheritance used like mobile class (parent class) is being used by sumsung and oneplus (child class)
# polymorphism = one thing used in a diff way like welcome statement as below
# datetime for showing time of purchase
# super function used as here extra parameter year is also to be passed

import datetime

class mobile:
    def __init__(self,brand,model):
        self.brandname = brand
        self.modelname = model

    def mobilename(self):
        print(f"brand : {self.brandname}")
        print(f"model : {self.modelname}")

    def print_year(self):
        print(f"year: {self.year}")

    def transaction_time(self):
        print(f"Transaction time: {datetime.datetime.now()}")
class sumsung(mobile):

    def __init__(self,brand,model):
        super().__init__(brand,model)
        self.year = 2020
    def welcome(self):
        print("welcome to sumsung")

class oneplus(mobile):

    def __init__(self,brand,model):
        super().__init__(brand,model)
        self.year = 2023

    def welcome(self):
        print("welcome to oneplus")



s1 = sumsung("sumsung","s20+")
op1 = oneplus("oneplus","7t")

for mobile in (s1, op1):
    mobile.welcome()
    mobile.mobilename()
    mobile.print_year()
    mobile.transaction_time()
    print("--------")

# print(s1.year)

