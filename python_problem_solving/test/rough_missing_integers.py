input_list = [1,2,3,6,7,8,4]
# how to do missing no in 10,11,12,14,15,16.....   ans 13

def missing_integers(input_list):
    n = len(input_list)+1
    actual_sum = sum(input_list)
    expected_sum = n*(n+1)/2
    return (expected_sum - actual_sum)

print(missing_integers(input_list))


input = [10,11,12,15,16,9]
def missing_int(input):
    for i in range(min(input), max(input)):
        if i not in set(input):
            return i


print(missing_int(input))

input1 = [10,11,12,15,16]
# def missing_int(input1):
#     output_list = []
#     set1 = set(input)
#     set2 = set(min(input1),max(input1))
#
#     for i in range(min(input), max(input)):
#         if i not in set:







