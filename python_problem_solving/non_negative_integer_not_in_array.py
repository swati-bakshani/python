# given an array arr of n unique non negative integers , how can you find a non- negative integer that is not in the array?

l=[0,1,2,3,4,5,8,9]

# l=[0,1,6,2,7,5,4]
#
# l=[3,1,6,2,7,5,4]
"""
output = 6.0
"""

"""
def find_missing_number(l):
    list_dict={}
    for i in l:
        list_dict[i]=True

    for i in range(len(l)):
    # for i in l:
        print(i,list_dict.get(i))
        if not list_dict.get(i):
            return i
    return None

print(find_missing_number(l))
"""
def missingNumber(input_list):
    sumN=0
    n=len(input_list)
    for num in input_list:
        sumN += num
        totalSum = n * (n + 1) / 2

        missing = totalSum - sumN
    return missing

input_list = [0, 1, 2, 3, 4, 5,6, 8, 9]
print(missingNumber(input_list))
