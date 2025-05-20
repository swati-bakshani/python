input = "Nikhil is a a good good boy and have a car"

def unique_words(inout):
    dict = {}
    output_list = []
    for word in input.split():
        if word in dict:
            dict[word] = dict[word]+1

        else:
            dict[word] = 1
    # print(dict)
    for k,v in dict.items():
        if v == 1:
            output_list.append(k)
    return output_list




output = unique_words(input)
print(output)