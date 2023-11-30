my_map = {
    'a':150,
    'b':75,
    'c':200,
    'd':50,
    'e':300
}

def dict_values(my_map):
    output_list=[]
    output_dict = {}
    for key,value in my_map.items():
        if value>100:
            output_list.append(value)
            output_dict[key] = value
    # return output_list
    return output_dict


print(dict_values(my_map))