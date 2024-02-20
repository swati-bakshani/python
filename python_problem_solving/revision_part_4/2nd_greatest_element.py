input_list = [20,30,40,100,400,300]

def second_greatest_elements(input_list):
    maximum_num = max(input_list)
    dict = {}
    for num in input_list:
        if (num!= maximum_num):
            dict[num] = maximum_num - num

    print(dict)
    return max(dict)

print(second_greatest_elements(input_list))


