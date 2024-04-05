# input = "nitin"
# def is_palindrome(input):
#     c=0
#     for letter in range(int(len(input)/2)):
#         if (input[letter] == input[len(input)-letter-1]):
#             continue
#         else:
#             c=1
#     return c == 0
#
# print(is_palindrome(input))

input1 = "Nitin"
input2 = "nitin"
def is_palindrome2(user_input):
    user_input = user_input.lower()
    c=0
    for letter in range(int(len(user_input)/2)):
        if (user_input[letter] == user_input[len(user_input)-letter-1]):
            continue
        else:
            c=1
    return c == 0

user_input = input("Enter your value:")

print(is_palindrome2(user_input))
# print(is_palindrome(input2))