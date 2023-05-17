class person:
    def __init__(self,firstname,lastname):
        self.fname = firstname
        self.lname = lastname

    def print_name(self):
        print(f"my name is {self.fname} {self.lname}")

class student(person):
    def hello(self):
        print("hello i m from student class")

o1 = student("swati", "bakshani")
o1.print_name()
o1.hello()