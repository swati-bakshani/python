# input1 = "nitin"

def is_palindrome(input):
    c=0
    len_str = len(input)
    for letter in range(int((len_str)/2)-1):
        if (input[letter] == input[len_str-letter-1]):
            continue
        else:
            c=1
    return c==0

user_input = input("Enter Your Value:")

print(is_palindrome(user_input))
