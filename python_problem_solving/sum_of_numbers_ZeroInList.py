l = [1,2,3,4,5,-1,-2,2,5,4]

def add_num(l):
    if len(l)<2:
        return False
    l1 = set(l)
    for i in l:
        if -i in l1:
            return True
    return False

l= [1,2,3,4,5,-1,-2,2,5,4]
l= [1,2,3,4,5,2,5,4]
print(add_num(l))