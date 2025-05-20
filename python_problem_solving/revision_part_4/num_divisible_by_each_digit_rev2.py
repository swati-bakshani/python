def num_divisibility(num):
    try:
        c=0
        for digits in str(num):
            if (num%(int(digits))==0):
                c=c+1
        return c
    except ZeroDivisionError:
        return len(str(num))


print(num_divisibility(12340))

def count_digits_divisible_by_number(number):
    original_number = number
    count = 0
    while number > 0:
        digit = number % 10
        if digit != 0 and original_number % digit == 0:
            count += 1
        number //= 10
    return count

number = 120450
print(count_digits_divisible_by_number(120450))
