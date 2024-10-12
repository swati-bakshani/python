def multiplication_table(input,x):
    for num in range(1,x+1):
        print(f"{input}*{num} = {input*num}")

print(multiplication_table(5,10))
