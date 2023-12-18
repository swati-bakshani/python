l = [1,2,4,5,6,7,8]

def missing_num(given_list):
    n = len(given_list)+1
    expected_sum = n * (n+1)/2
    actual_sum = sum(given_list)
    return (expected_sum - actual_sum)

print(missing_num(l))

