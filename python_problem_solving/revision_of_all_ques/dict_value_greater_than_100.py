my_map = {
    'a':150,
    'b':75,
    'c':200,
    'd':50,
    'e':300
}
def value_greater_100(my_map,user_input):
    output_list=[]
    for key,value in my_map.items():
        if value > user_input:
            output_list.append(value)
    return output_list

user_input = int(input("enter the value:"))
print(value_greater_100(my_map,user_input))



# print(dict_values(my_map))