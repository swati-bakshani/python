input_list = [1,2,3,1,5,1,2,4,6,6]

def count_freq(input_list):
    dict = {}
    output_list = []
    for num in input_list:
        if num in dict:
            dict[num] = dict[num]+1
        else:
            dict[num] = 1

    return dict

print(count_freq(input_list))

def count_freq1(input_list):
    freq = {}
    for num in input_list:
        freq[num]=freq.get(num,0)+1

    return freq

print(count_freq1(input_list))


