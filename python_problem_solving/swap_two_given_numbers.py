# swap two given numbers

# 5,6 ..... >6,5

def swap(a,b):
    c=a
    a=b
    b=c
    return (a,b)

print(swap(5,6))

def swap_1(a,b):
    """
    swap function to swap the value
    """
    a,b=b,a
    return (a,b)

# print(swap_1(10,3))
get_input_1 = input("Enter First Value: ")
get_input_2 = input("Enter second Value: ")
result = swap_1(get_input_1,get_input_2)
print(f"Your result is : {result}")