input_list = [1,3,2,5,6,7,5,3,2,1,8]
"""
output: {1: 2, 2: 2, 3: 2, 5: 2, 6: 1, 7: 1, 8: 1}
"""
def counter(input_list):
    input = sorted(input_list)
    freq = {}
    for num in input:
        freq[num] = freq.get(num,0)+1
        print(num,freq[num])

    return freq

print(counter(input_list))