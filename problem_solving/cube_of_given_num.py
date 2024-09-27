input_list = [1,2,3,4,5,6]

def Cube_of_num(l):
    output_list = []
    for num in l:
        cube = num*num*num
        output_list.append(cube)
    return output_list

print(Cube_of_num(input_list))

print('......cube of odd numbers......')
def Cube_of_num(l):
    output_list = []
    for num in l:
        if num%2 == 1:
            cube = num*num*num
            output_list.append(cube)
    return output_list

print(Cube_of_num(input_list))

print('......cube of even numbers.....')
def Cube_of_num(l):
    output_list = []
    for num in l:
        if num%2 == 0:
            cube = num*num*num
            output_list.append(cube)
    return output_list

print(Cube_of_num(input_list))




