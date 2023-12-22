input_list = [1,2,3,5,10,20,30,15]

def second_greatest_num(input_list):
    largest_num = max(input_list)
    dict = {}
    for num in input_list:
        if (num!= largest_num):
            dict[num] = largest_num-num

    return max(dict)

print(second_greatest_num(input_list))
