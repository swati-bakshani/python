input_list = [1,2,3,1,5,1,2,4,6,6]
def counter(input_list):
    freq = {}
    for num in input_list:
        freq[num]=freq.get(num,0)+1
        print(num,freq[num])

    return freq

print(counter(input_list))