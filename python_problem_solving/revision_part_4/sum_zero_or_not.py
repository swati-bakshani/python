list = [1,2,4,5,7,2,5,-3] # --false
list1 = [1,2,4,5,7,2,5]  # --false
list2 = [1,2,4,5,7,2,5,-2,-1]  # --true

def sum_zero(input_list):
    if len(input_list)<2:
        return False
    unique_num = set(input_list)
    print(unique_num)
    for num in input_list:
        if -num in unique_num:
            return True
    return False

if __name__ == '__main__':
    print(sum_zero(list))