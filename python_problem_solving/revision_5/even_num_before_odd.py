
list = [1,2,3,4,5,7,6,8,5,2]
def even_before_odd(list):
    output_list =[]
    for num in range(len(list)-1):
        if (list[num]%2==0 and list[num+1]%2==1):
            output_list.append(list[num])

    return output_list

output = even_before_odd(list)
print(output)
