# def even_num_square(list):
#     for i in list:
#         if i%2 == 0:
#             a=i*i
#             return a
#
# print(even_num_square([1,2,3,4,5,6,7,8]))

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# output: even no squares
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even_no_square(list):
    output=[]
    for i in list:
        if i % 2 == 0:
            a = i * i
            output.append(a)
    return output


print(even_no_square(list))