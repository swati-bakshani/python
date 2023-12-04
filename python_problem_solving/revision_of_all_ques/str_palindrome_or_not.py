str = 'aabbaa'


def palindrome(str):
    c=0
    for letter in range(int(len(str)/2)):
        if (str[letter] == str[len(str)-letter-1]):
            continue
        else:
            c=1
    return c==0

print(palindrome(str))
