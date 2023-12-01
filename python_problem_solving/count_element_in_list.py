list = [1,2,3,4,5,6]
"""
output = 6
"""
# def count_len_list(list):
#     print(len(list))

# count_len_list(list)

"""
Using Recursive
"""
def count_len_list(list):
    if not list:
        return 0
    return 1+count_len_list(list[1:])

print(count_len_list(list))

