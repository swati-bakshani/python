my_map = {
    'a':150,
    'b':75,
    'c':250,
    'd':50,
    'e':400
}
def dict_value(my_map):
    dict = {}
    output_list = []
    for key,value in my_map.items():
        if value > 100:
            output_list.append(value)
            dict[key] = value
    return dict
    # return output_list .... .. [150,250,400]

print(dict_value(my_map))
