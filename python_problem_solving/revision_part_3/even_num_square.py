list = [1,2,3,4,8,7,9,0]

def even_num_sq(list):
    output_list = []
    for num in list:
        if (num%2 == 0):
            even_num_sq = num*num
            output_list.append(even_num_sq)
    return output_list

print(even_num_sq(list))
