input_list = [1,2,3,4,7,8,9,14,6]

def even_num_square(input_list):
    output_list = []
    for num in input_list:
        if num%2 == 0:
            even_num = num*num
            output_list.append(even_num)

    return output_list

output = even_num_square(input_list)
print(output)
