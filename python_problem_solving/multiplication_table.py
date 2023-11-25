"""
write a method that takes a number as parameter and generates multiplication table for it
example:
5*1 = 5
5*2 = 10
"""
def multiplication_table(num,x):
    for i in range(1,x+1):
        print(f"{num}*{i} = {i*num}")
        # print(f"{num}*{i}","=",f"{num*i}")
multiplication_table(5,20)