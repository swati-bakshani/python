input_list = [1,2,3,4,6,7,8]
# how to do missing no in 10,11,12,14,15,16.....   ans 13
def missing_integer(input_list):
    n = len(input_list)+1
    expected_sum = n*(n+1)/2
    actual_sum = sum(input_list)
    return (expected_sum - actual_sum)

print(missing_integer(input_list))