input_list = [1,2,3,4,5,-1,-2,2,5,4]

def sum_zero(input_list):
    if len(input_list)<2:
        return False
    unique_values = set(input_list)
    for num in input_list:
        if num in unique_values:
            return True
    return False

if __name__ == '__main__':
    print(sum_zero(input_list))

