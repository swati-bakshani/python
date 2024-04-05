list = [1,2,3,4,5,2,5,4,]

def sum_zero_or_not(list):

    unique_num = set(list)
    for num in list:
        if -num in unique_num:
            return True

    return False

print(sum_zero_or_not(list))