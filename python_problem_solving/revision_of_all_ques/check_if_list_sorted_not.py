l1 = [1,2,3,4,5,3]

def sorted_list(l1):
    k=0
    for num in range(len(l1)-1):
        if l1[num]<=l1[num+1]:
            pass
        else:
            k=1
            break

    return k == 0

print(sorted_list(l1))