
l=[1,2,4,5,3,6,5]
l1 = [1,2,4,5,6,7]
"""
l  output = False
l1 output = true
"""
def sorted_list(l):
    k=0
    for num in range(len(l)-1):
        if (l[num] <= l[num+1]):
            pass
        else:
            k=1
            break
    return k==0

print(sorted_list(l))
print(sorted_list(l1))