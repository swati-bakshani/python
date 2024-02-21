l=[1,2,4,5,3,6,5]
l1 = [1,2,4,5,6,7]

def sorted_list(l1):
    c=0
    for num in range(len(l1)-1):
        if l1[num]<=l1[num+1]:
            pass
        else:
            c=1
            break
    return c==0

print(sorted_list(l1))