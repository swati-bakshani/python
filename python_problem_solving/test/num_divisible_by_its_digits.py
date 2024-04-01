# input = 123678

def num_divisibility(user_input):

    try:
        n=0
        for digit in str(user_input):
            if user_input%int(digit) == 0:
                n = n+1
        return n
    except ZeroDivisionError:
        return len(str(user_input))

user_input = input("Enter your value:")

print(num_divisibility(int(user_input)))

