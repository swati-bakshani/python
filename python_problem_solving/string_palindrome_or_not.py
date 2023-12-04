# str ='sagar'   #ragas
# str ='abba'  #abba
# False
# True
def is_palindrome(str):
    len_str = len(str)
    c=0
    for i in range(int(len_str/2)):
        if (str[i]==str[len_str-i-1]):
            continue
        else:
            c=1
    return c==0
#

print(is_palindrome('abefba'))
print(is_palindrome('abba'))
# get_data = input("Enter the Value: ")
# result = is_palindrome(get_data)
# print(f"result is: {result}")
