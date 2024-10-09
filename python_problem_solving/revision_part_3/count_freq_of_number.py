input_list = [1,2,3,1,5,1,2,4,6,6]

def count_freq(input_list):
    dict = {}
    for num in input_list:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] = dict[num]+1
    return dict

print(count_freq(input_list))
