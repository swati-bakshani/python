input = 'nitin'
input1 = 'nikhil'

def is_palindrome(word):
    c=0
    for letter in range(int(len(word)/2)):
        if (word[letter] == word[int(len(word))-letter-1]):
            continue
        else:
            c=1

    return c==0

print(is_palindrome(input1))