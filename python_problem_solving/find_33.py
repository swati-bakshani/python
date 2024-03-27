def has33(num_list):
    index = 0
    for number in num_list:
        if number==3:
            if index == 0:
                if num_list[index+1]==3:
                    return True
            elif index == len(num_list)-1:
                if num_list[index-1] == 3:
                    return True
            else:
                if num_list [index+1] == 3:
                    return True

print(has33([2,4]))

