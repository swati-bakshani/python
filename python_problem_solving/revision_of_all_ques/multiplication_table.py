def multiplication_table(num,x):
    for i in range(1,x+1):
        print(f"{num} * {i} = {num*i}")

print(multiplication_table(5,10))