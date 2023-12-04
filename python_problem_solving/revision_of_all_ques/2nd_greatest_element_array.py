l = [1,2,3,5,7,8,9,6,5,3,4]

def second_greatest(l):
    max_num = max(l)
    dict = {}
    for num in l:
        if (num!= max_num):
            dict[num] = max_num-num
    print(dict)
    return max(dict)

result = second_greatest(l)
print(result)
