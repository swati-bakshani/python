my_map = {
    'a':150,
    'b':75,
    'c':250,
    'd':50,
    'e':400
}

def dict_value(my_map,user_input):
    output_list = []
    for key,value in my_map.items():
        if value > user_input:
            output_list.append(value)

    return output_list

# user_input = int(input("Enter the Value: "))
# print(dict_value(my_map,user_input))

def dict_value_nick(my_map,user_input):
    output_list = []
    result = {}
    for key,value in my_map.items():
        if value > user_input:
            result[key] = value
            # output_list.append(value)

    return result

user_input = int(input("Enter the Value: "))
print(dict_value_nick(my_map,user_input))

# def dict_key_value(my_map,user_input):
#     output_dict = {}
#     for key,value in my_map.items():
#         if value > user_input:
#             output_dict.append(key,value)
#
#     return output_dict
#
# user_input = int(input("Enter the Value: "))
# print(dict_key_value(my_map,user_input))