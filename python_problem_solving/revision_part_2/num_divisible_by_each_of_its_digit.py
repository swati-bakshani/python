# given_input = 123

def num_divisibility(given_input):
    try:
        c=0
        for num in str(given_input):
            if (given_input%int(num)==0):
                c=c+1
        return c
    except ZeroDivisionError:
        return len(str(given_input))

print(num_divisibility(12345))

def digits_divisibility(given_num):
    try:
        c=0
        for number in str(given_num):
            if (given_num%int(number)==0):
                c=c+1
        return c
    except ZeroDivisionError:
        return len(str(given_num))

print(digits_divisibility(123456))
print(digits_divisibility(12304567))

