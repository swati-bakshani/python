input_string = "geekcoders geekcoders hello"

def count_words(input_list):
    dict = {}
    for word in input_string.split():
        if word in dict:
            dict[word] = dict[word]+1
        else:
            dict[word] = 1
    return dict

print(count_words(input_string))
print(len(input_string))