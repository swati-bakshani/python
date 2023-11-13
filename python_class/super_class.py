class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def print_year(self):
        print(f"my graduation year is {self.graduationyear}")

    def print_student_details(self):
        print(f"my name is {self.firstname} {self.lastname}. I graduated in {self.graduationyear}")

x = Student("Mike", "Olsen", 2019)
# print(x.firstname, x.lastname)
x.printname()
x.print_year()
x.print_student_details()
