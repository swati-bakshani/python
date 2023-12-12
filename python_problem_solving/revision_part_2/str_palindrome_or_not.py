input_str = 'abba'
str = 'nikhil'
def str_palimdrome(word):
    c=0
    len_str = len(word)
    for letter in range(int(len_str/2)):
        if (word[letter] == word[len_str-letter-1]):
            continue
        else:
            c=1
    return c==0

print(str_palimdrome(input_str))
print(str_palimdrome(str))
