input_list = [1,2,3,4,6,7,8]

def list_sorted(input_list):
    c=0
    for num in range(len(input_list)-1):
        if input_list[num]<input_list[num+1]:
            pass
        else:
            c = 1
            break

    return c==0

print(list_sorted(input_list))

