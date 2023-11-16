# WAP to insert a string in middle of a given string

# below string is given as input
# str_place = 'City:kolkata-westbengal'

def add_str(input_str):
    return input_str.replace("-","-State:")
str_place = 'City:kolkata-westbengal'
print (add_str(str_place))

# def add_str(input_str):
#     f_index = input_str.find('westbengal')
#     print(f_index)
#     # return input_str.replace("-","-State:")
# str_place = 'City:kolkata-westbengal'
# print (add_str(str_place))