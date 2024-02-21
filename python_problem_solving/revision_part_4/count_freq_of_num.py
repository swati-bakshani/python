input_list = [1,2,3,1,5,1,2,4,6,6]

def count_freq(input_list):
    freq = {}
    for num in input_list:
        if num in freq:
            freq[num] = freq[num]+1
        else:
            freq[num] = 1

    return freq

print(count_freq(input_list))
