input = "Nikhil is is a good boy boy"

def unique_words(input):
    dict = {}
    output_list = []
    for word in input.split():
        if word in dict:
            dict[word]= dict[word]+1
        else:
            dict[word] = 1

    print(dict)

    for k,v in dict.items():
        # if v == 1:
            output_list.append(k)
    return output_list

output = unique_words(input)
print(output)

""" print every word once"""

    # for k, v in dict.items():
    #     if v == 1:
    #         output_list.append(k)
    # return output_list
