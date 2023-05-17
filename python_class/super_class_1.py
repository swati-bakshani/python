class person:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname

class student(person):
    def __init__(self,firstname, lastname, graduation_year):
        super().__init__(firstname,lastname)
        self.graduation_year = graduation_year
        self.college = "Dimat"

    def welcome(self):
        print(f"welcome to the class of {self.graduation_year} {self.fname} {self.lname} in {self.college}")


student1 = student("swati", "bakshani", 2019)
student1.welcome()