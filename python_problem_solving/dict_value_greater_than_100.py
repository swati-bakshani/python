my_map = {
    'a':150,
    'b':75,
    'c':200,
    'd':50,
    'e':300
}
def get_value(my_map,value):
    l=[]
    for k,v in my_map.items():
        if(v>value):
                l.append(v)
    return l
            # print(k,v)

print(get_value(my_map,100))