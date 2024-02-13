list = [1,2,4,5,7,8,10,11,12,14,15]

def even_before_odd(list):
    output_list = []
    for num in range(len(list)-1):
        if (list[num]%2==0 and list[num+1]%2==1):
            # output_list.append(num).. .. if we want to now the position than this is right positions = [2,6,9]
            output_list.append(list[num])
    return output_list

print(even_before_odd(list))