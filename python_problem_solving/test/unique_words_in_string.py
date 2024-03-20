
input_str= "john is a a boy"
def unique_words(input_str):
    dict = {}
    output_list = []
    for word in input_str.split():
        if word in dict :
            dict[word] = dict[word]+1
        else:
            dict[word] = 1
    print(dict)
    for k,v in dict.items():
        if v == 1:
            output_list.append(k)
    return output_list

print(unique_words(input_str))