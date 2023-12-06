l=[1,2,3,4,5,-1,-2,-3,2,5,4,-6]

def add_num_zero(l):
    if len(l)<2:
        return False
    l1 = set(l)
    for i in l:
        if -i in l1:
            return True

    return False
print(add_num_zero(l))
