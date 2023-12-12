list = [1,2,3,4,100,5,600]
"""
output = 600
"""
def largest_num(data):
    largest = data[0]

    for num in data:
        if num > largest:
            largest = num

    return largest

print(largest_num(list))