my_dict = {
    'a':150,
    'b':75,
    'c':250,
    'd':50,
    'e':400
}
#  2 ways to do this ques both are correctjn
def dict_greater_100(my_dict,user_input):
    # output_list = []
    output_dict = {}
    for key,value in my_dict.items():
        if value>user_input:
            # output_list.append(value)
            output_dict[key] = value

    return output_dict

user_input = int(input("Enter Your Value:"))

print(dict_greater_100(my_dict,user_input))