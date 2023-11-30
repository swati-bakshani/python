input_list = [1,2,3,4,5,6,7,8]

def even_num_square(input_list):
    output_list=[]
    for num in input_list:
        if (num%2==0):
            even_num = num*num
            output_list.append(even_num)
    return output_list

print(even_num_square(input_list))

"""
odd no square
"""
def odd_num_square(input_list):
    output_list=[]
    for num in input_list:
        if (num%2==1):
            odd_num = num*num
            output_list.append(odd_num)
    return output_list

print(odd_num_square(input_list))