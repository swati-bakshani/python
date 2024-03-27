# input = "nikhil is is a data engineer"

# def remove_duplicate(input):
#     output_list = []
#     for word in input.split():
#         unique = set(input.split())
#     #     if word in unique:
#     #         output_list.append(word)
#     # return output_list
#
# print(remove_duplicate(input))
input = "nikhil is is a data engineer"
def remove_duplicate(input):
    output_list = []
    for word in input.split():
        if word not in output_list:
            output_list.append(word)

    return output_list

print(remove_duplicate(input))