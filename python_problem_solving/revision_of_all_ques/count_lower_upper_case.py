input_str = "Swati Weds Nikhil"
"""
output = (12, 3)
<class 'tuple'>
"""
def count_char(input_str):
    count_lower,count_upper = 0,0
    for char in input_str:
        if char.islower():
            count_lower = count_lower+1
        elif char.isupper():
            count_upper = count_upper+1
    return count_lower,count_upper

print(count_char(input_str))

