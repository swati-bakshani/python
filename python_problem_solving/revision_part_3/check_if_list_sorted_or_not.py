
l=[1,2,4,5,3,6,5]
l1 = [1,2,4,5,6,7]
"""
l  output = False
l1 output = true
"""
def list_sorted(input_list):
    c=0
    for num in range(len(input_list)-1):
        if input_list[num] <= input_list[num+1]:
            pass
        else:
            c=1
            break
    return c==0

print(list_sorted(l1))