list = "NIKHIL is a Super Man my aji oji"

def count_char(list):
    c=0
    count_lower,count_upper = 0,0
    for char in list:
        if (char.islower()):
            count_lower = count_lower+1

        elif (char.isupper()):
            count_upper = count_upper+1

    return (count_lower,count_upper)

print(count_char(list))