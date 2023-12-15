def find_factorial(num):
    """
    output of factorial of 5 = 120
    """
    fact = 1
    while num > 0:
        fact = fact*num
        num = num - 1
    return fact

user_input = int(input("Enter Your Input Here: "))
print(find_factorial(user_input))
