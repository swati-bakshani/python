class person:
    def __init__(self,name,age):
        self.student_name = name
        self.age = age
        self.college = "Dimat"
        self.college_city = "Raipur"

p1 = person("swati",29)
p2 = person("Nikhil",31)

print(p1.student_name,p2.student_name)
print(p1.age)
print(p1.college)
print(f"my name is {p1.student_name}, age is {p1.age} and college is {p1.college} and i am from {p2.college_city}")