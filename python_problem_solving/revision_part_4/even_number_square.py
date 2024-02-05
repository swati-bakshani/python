input_list = [1,2,5,6,8,7,9,3]

def even_number_square(input_list):
    output_list = []
    for num in input_list:
        if num%2==0:
            even_num = num*num
            output_list.append(even_num)
    return output_list

print(even_number_square(input_list))

def even_number_square(input_list):
    output_list = []
    for num in range(len(input_list)):
        if input_list[num]%2==0:
            even_num = input_list[num]*input_list[num]
            output_list.append(even_num)
    return output_list

print(even_number_square(input_list))