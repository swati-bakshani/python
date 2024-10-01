num_list = [5,2,3,2,3,4,9,1,5]

"""
output = 
{5: 4, 2: 7, 3: 6, 4: 5, 1: 8}
5
"""

def second_gretest_element(input_list):
    dict = {}
    largest_num = max(input_list)
    for num in input_list:
        if num != largest_num:
            dict[num] = largest_num - num
    return max(dict)

print(second_gretest_element(num_list))