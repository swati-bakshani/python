# given_input = 123

def num_divisibility(user_input):
    try:
        c=0
        for num in str(user_input):
            if user_input%int(num)==0:
                c=c+1
        return c
    except ZeroDivisionError:
        return len(str(user_input))

user_input = input("Enter your Value:")
print(num_divisibility(int(user_input)))