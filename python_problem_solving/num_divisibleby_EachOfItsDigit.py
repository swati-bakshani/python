# To find given no given no is divisible by each of its digit or not

# lets take example  124
#   124 is divisible by all of its digits i.e. 1 , 2 and 4 also.
#   so we have to print total counts i.e. 3 in this case.
# if its 120 then ZeroDivisionError execption will come
#   and then we have to print count o digits , output is 2 as 120 is divisible by 1,2 in its number.


def f_digits_divisibility(num):
    try:
        c=0
        for i in str(num):
            if(num%int(i)==0):
                c=c+1
        return c
    except ZeroDivisionError:
        return len(str(num))

print(f_digits_divisibility(120))


