# str ='sagar'   #ragas
# str ='abba'  #abba
# False
# True
def is_palindrome(str):
    len_str = len(str)
    c=1
    for i in range(int(len_str/2)):
        if (str[i]==str[len_str-i-1]):
            continue
        else:
            c=0
    return c==1
#

# print(is_palindrome('abefba'))
# print(is_palindrome('abba'))
if __name__ == '__main__':
    get_data = input("Enter the Value: ")
    result = is_palindrome(get_data)
    print(f"result is: {result}")
