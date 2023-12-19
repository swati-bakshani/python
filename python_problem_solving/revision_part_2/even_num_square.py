input_list = [1,2,4,5,6,7,8,3,10,11,12]
def even_num_square(input_list):
    output_list= []
    for num in input_list:
        if num%2 == 0:
            even_num = num*num
            output_list.append(even_num)
    return output_list

print(even_num_square(input_list))