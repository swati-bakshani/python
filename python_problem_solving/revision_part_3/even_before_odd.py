List = [1,2,3,4,8,7,9,2,7,0]

def even_before_odd(list):
    output_list = []
    output_list_square = []
    for num in range(len(list)-1):
        if (list[num]%2 == 0 and list[num+1]%2 == 1):
            even_num_square = list[num]*list[num]
            even_num = list[num]
            output_list.append(even_num)
            output_list_square.append(even_num_square)
    return output_list
    # return output_list_square


print(even_before_odd(List))