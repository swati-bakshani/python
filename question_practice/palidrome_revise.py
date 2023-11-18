# abba

def is_palidrome(str):
    len_str=len(str)
    c=0
    for i in range(int(len_str/2)):
        if (str[i]==str[len_str-i-1]):
            continue
        else:
            c=1
    return c==0

print (is_palidrome('abba'))
