class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.college = "Dimat"
        self.college_city = "Raipur"


    def print_details(self):
        print(f"my name is {self.name}, age is {self.age} and college is {self.college}")

p1 = person("swati",29)
p2 = person("Nikhil",31)

# print(p1.name)
# print(p1.age)
# print(p1.college)
# print(f"my name is {p1.name}, age is {p1.age} and college is {p1.college}")
p1.print_details()
p2.print_details()