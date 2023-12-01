test_1 = [1,2,3,4,5]
test_2 = [1,2,3,3,4,4,5]
test_3 = [1,2,4,5,3,6,5]
"""
output : True or False
"""
def sorted_list(input_list):
    k=0
    for num in range(len(input_list)-1):
        if (input_list[num]<=input_list[num+1]):
            pass
        else:
            k=1
            break

    return k==0

print(sorted_list(test_3))

# second method
def check_sorted_list(input_list):
    return  all(input_list[num]<=input_list[num+1] for num in range(len(input_list)-1))

print(check_sorted_list(test_3))
