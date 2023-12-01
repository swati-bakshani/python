list = [1,4,0,2,3,5,6]

"""
Using Recursive
"""
def count_elements(list):
    if not list:
        return 0
    return 1+count_elements(list[1:])

print(count_elements(list))

