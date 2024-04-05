input_list = [1,2,3,4,5,7,8]

def missing_integer(input_list):
    for num in input_list:
        n = len(input_list)+1
        actual_sum = sum(input_list)
        expected_sum = n*(n+1)/2
        return (expected_sum - actual_sum)

print(missing_integer(input_list))

