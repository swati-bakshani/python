l = [1,2,3,4,6,7,8,9]

def missing_no(l):
    n = len(l)+1
    expected_sum = n * (n+1) / 2
    actual_sum = sum(l)
    return (expected_sum - actual_sum)

print(missing_no(l))

"""
def find_missing(arr,num):
    arr = []
    num = int(input("Enter the lenght of the array"))
    for int in range(num-1):
        m = int(input("Enter the element/number"))
        arr.append(m)

    missing_num = find_missing(arr,num)
    print(f"The missing num is {missing_num}")
"""
# wrong ans
# def find_missing_no(l):
#     for i in l:
#         if i<i+1:
#             pass
#         else:
#             break
#     return i
# l1= [1,2,3,5,7,4]
# print(find_missing_no(l1))

