num_list = [5,2,3,2,3,4,9,1,5]

"""
output = 
{5: 4, 2: 7, 3: 6, 4: 5, 1: 8}
5
"""
# def greatest_element(num):
#     for element in len(num):
#         if [element] > [element+1]:

# Greatest no
#         max_num=max(num)
#         print(max_num)

# 2nd smallest no.in the array

# min_smallest=min(num_list)
# dict={}
# for i in num_list:
#     if (i!=min_smallest):
#         dict[i]=i-min_smallest
#
# print(dict)
# print(min(dict))

# 2nd greatest num in num_list
"""
output = 
{5: 4, 2: 7, 3: 6, 4: 5, 1: 8}
5
"""
max_greatest= max(num_list)
dict={}
for i in num_list:
    if (i!=max_greatest):
        dict[i]=max_greatest-i

print(dict)
print(max(dict))


