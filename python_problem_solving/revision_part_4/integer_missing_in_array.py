input_list = [1,2,3,4,6,7,8]
input_list2 = [10,11,12,14,15,16]
print(input_list2[-2])
# how to do missing no in 10,11,12,14,15,16.....   ans 13
# def missing_num(input_list):
#     n = max(input_list)
#     actual_sum = sum(input_list)
#     expected_sum = (n*(n+1))/2
#     return (expected_sum - actual_sum)

def missing_integer(input_list):
    # print(len(input_list)-1)
    for num in range(len(input_list)-1):
        # print(num)
        # print(input_list[num-1])
        if (input_list[num] - input_list[num-1] != 1):
            missing_num = input_list[num]-1
    return missing_num

# print(missing_num(input_list))
# print(missing_integer(input_list))
# print(missing_num(input_list2))
# print(missing_integer(input_list2))

# def missing_number(input_list):
#
#     actual_sum = sum(input_list)
#     expected_sum = sum(range(min(input_list),max(input_list)+1))
#     print(expected_sum)
#     return (expected_sum - actual_sum)
#
#
# print(missing_number(input_list2))