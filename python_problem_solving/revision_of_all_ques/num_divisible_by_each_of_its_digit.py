def digit_divisibility(num):
    try:
        c=0
        for n in str(num):
            if (num%int(n)==0):
                c=c+1
        return c
    except ZeroDivisionError:
        return len(str(num))

print(digit_divisibility(1234))

