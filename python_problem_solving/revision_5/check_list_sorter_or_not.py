l1 = [1,2,3,4,5]

def list_sorted(l1):
    c=0
    for num in range(len(l1)-1):
        print(num)
        if l1[num] < l1[num+1]:
            pass

        else:
            c = 1
            break


    return c == 0

print(list_sorted(l1))
