list = [1,2,3,4,5,8,9]

def even_num(list):
    output_list = []
    for num in list:
        if num%2 == 0:
            even_num = num*num
            output_list.append(even_num)
    return output_list

print(even_num(list))
