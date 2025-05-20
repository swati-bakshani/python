# def num_divisibility(input_num):
#     try:
#         c=0
#         for num in str(input_num):
#             if (input_num%int(num)==0):
#                 c=c+1
#         return c
#
#     except ZeroDivisionError as e:
#         # return len(str(input_num))
#         print(f"invalid input: {e}")
#
# print(num_divisibility(12340))
#
# def count_digits_divisible_by_number(number):
#     original_number = number
#     count = 0
#     while number > 0:
#         digit = number % 10
#         if digit != 0 and original_number % digit == 0:
#             count += 1
#         number //= 10
#     return count
#
# number = 120450
# result = count_digits_divisible_by_number(number)
# print(f"Count of digits in {number} that are divisible by {number}: {result}")
#
# 
#

numbers = [1, 2, 3, 4, 5]
result = numbers[1:4]  # Slicing
print(result)