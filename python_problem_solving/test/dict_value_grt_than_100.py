my_map = {
    'a':150,
    'b':75,
    'c':250,
    'd':50,
    'e':400
}
def value_greater_100(dict,value):
    output_list = []
    for k,v in dict.items():
        if v > int(value):
            output_list.append(v)
    return output_list

value = input("enter your value:")

print(value_greater_100(my_map,value))

def value_greater_100(dict,value):
    output_dict = {}
    for k,v in dict.items():
        if v > int(value):
            output_dict[k] = v
    return output_dict

value = input("enter your value:")

print(value_greater_100(my_map,value))