input_list = "geekcoders GEEKcoders ARe good"

def count_lower_upper_case(input_list):
    count_lower,count_upper = 0,0
    for letter in input_list:
        if letter.islower():
            count_lower = count_lower + 1
        elif letter.isupper():
            count_upper = count_upper + 1
    return count_lower,count_upper

print(count_lower_upper_case(input_list))
