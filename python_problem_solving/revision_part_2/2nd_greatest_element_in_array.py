input_list = [20,30,40,100,400,300]
def second_greatest(input_list):
    largest_num = max(input_list)
    dict = {}
    for num in input_list:
        if (num!= largest_num):
            dict[num]= largest_num-num
    print(dict)
    return max(dict)

print(second_greatest(input_list))



