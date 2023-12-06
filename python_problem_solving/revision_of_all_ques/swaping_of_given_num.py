def swap(a,b):
    a, b = b, a
    return a,b

print(swap(1,2))

get_first_num = input("Enter First Number: ")
get_second_num = input("Enter second Number: ")
output = swap(get_first_num,get_second_num)

print(output)
print(f"your answer is : {output}")