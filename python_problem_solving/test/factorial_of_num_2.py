input = 5

def factorial_num(num):
    fact = 1
    if num == 0:
        fact = 1
    while num>0:
        fact = fact*num
        num = num-1

    return fact

print(factorial_num(0))

# def factorial_num(num):
#     fact = num
#     while fact>0:
#         fact = fact*(fact-1)
#
#
#     return fact
#
# print(factorial_num(5))


