import datetime
class car:
    def __init__(self, brandname, modelname):
        self.brand = brandname
        self.model = modelname
        # self.city = "Raipur"

    def welcome(self):
        print(f"welcome to our car family")

    def transaction_time(self):
        print(f"transaction time : {datetime.datetime.now()}")

    def print_details(self):
        print(f"Brand Name = {self.brand}")
        print(f"Model Name = {self.model}")


class kia(car):
    def __init__(self, brandname, modelname, customer_name):
        super().__init__(brandname, modelname)
        self.name = customer_name
        # self.city = city

    # def print_details(self):
    #     print(f"Brand Name = {self.brand}")
    #     print(f"Model Name = {self.model}")
    #     print(f"customer_name = {self.name}")
    #     print(f"city = {self.city}")

    def welcome(self):
        print(f"welcome to our kia family Mr. {self.name} ")


class maruti(car):
    pass


car1 = kia("kia", "sonnet","nikhil")
car2 = maruti("maruti", "swift")

for vehicles in (car1, car2):
    vehicles.welcome()
    vehicles.print_details()
    vehicles.transaction_time()