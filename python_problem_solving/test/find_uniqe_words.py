
input_str = "delhi is is a a capital of of india"
def find_unique_words(input_str):
    dict = {}
    output_list = []
    for word in input_str.split():
        if word in dict:
            dict[word] = dict[word]+1
        else:
            dict[word] = 1

    for k,v in dict.items():
        if v == 1:
            output_list.append(k)
    return output_list

print(find_unique_words(input_str))

