# input_str= " Nikhil Is a GooD Boy"
#
# def count_upper_lower_char(input_str):
#     upper,lower = (0,0)
#
#     for char in input_str:
#         if (char.islower()):
#             lower = lower+1
#         elif (char.isupper()):
#             upper = upper+1
#     return (upper,lower)
#
# print(count_upper_lower_char(input_str))

def count_upper_lower_char(input_str):
    upper,lower = (0,0)

    for char in input_str:
        if (char.islower()):
            lower = lower+1
        elif (char.isupper()):
            upper = upper+1
    return (upper,lower)

input_str = input("Enter your Statement:" )

print(count_upper_lower_char(input_str))
upper, lower = count_upper_lower_char(input_str)
print(f"count of Lower Char is {lower} and upper char is {upper}")



