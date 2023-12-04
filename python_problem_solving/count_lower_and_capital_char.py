input_str = "Hello this is GeekCoders"
"""
output = (18, 3)
<class 'tuple'>
"""
def count_chars(input_str):
    cnt_lower,cnt_upper=0,0
    for char in input_str:
        if (char.islower()):
            cnt_lower = cnt_lower + 1
        elif (char.isupper()):
            cnt_upper = cnt_upper + 1
    return cnt_lower,cnt_upper

print(count_chars(input_str))

print(type(count_chars(input_str)))


# 2nd way of solving the problem

# def count_char(input_str):
#     lambda (filter(input_str:input_str.islower(),input_str.isupper))
#         if (char.islower()):
#             cnt_lower = cnt_lower + 1
#         elif (char.isupper()):
#             cnt_upper = cnt_upper + 1
#     return cnt_lower,cnt_upper

