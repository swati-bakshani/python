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

user_input = int(input("Enter the Value: "))
print(dict_value(my_map,user_input))