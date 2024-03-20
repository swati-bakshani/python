input_list = [1,2,3,4,5,6,7,10,12]
def even_before_odd(input_list):
    output_list = []
    for num in range(len(input_list)-1):
        if (input_list[num]%2==0 and input_list[num+1]%2==1):
            output_list.append(input_list[num])
    return output_list

print(even_before_odd(input_list))

list = [1,2,3,4,5,6,7,10,12]
def even_before_odd(list):
    output_list = []
    for num in range(len(list)-1):
        if (list[num]%2==0 and list[num+1]%2==1):
            output_list.append(list[num])
    return output_list

print(even_before_odd(input_list))