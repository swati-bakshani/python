def swap_number(a,b):
    c=a
    a=b
    b=c
    return a,b

print(swap_number(1,2))

def swap_number1(c,d):
    c,d = d,c
    return c,d

print(swap_number1(1,2))