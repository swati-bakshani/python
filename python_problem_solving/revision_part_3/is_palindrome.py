input = 'nitin'
input1 = 'nikhil'

def is_palindrome(input):
    c=0
    for letter in range(int(len(input)/2)):
        if (input[letter] == input[int(len(input))-letter-1]):
            continue
        else:
            c=1
    return c == 0

print(is_palindrome(input1))