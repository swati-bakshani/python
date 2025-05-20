num_list = [5,2,3,2,3,4,9,1,5]

def second_greatest(num_list):
    largest = max(num_list)
    dict = {}
    for num in num_list:
        # if num < largest:
            dict[num] = (largest - num)

    print(dict)

    return max(dict)

print(second_greatest(num_list))



