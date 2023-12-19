input_list = [1,2,4,5,6,7,8,3,10,12,11]

def even_before_odd(input_list):
    output_list = []
    for num in range(len(input_list)-1):
        if (input_list[num]%2==0 and input_list[num+1]%2==1):
            output_list.append(input_list[num])

    return output_list

print(even_before_odd(input_list))

