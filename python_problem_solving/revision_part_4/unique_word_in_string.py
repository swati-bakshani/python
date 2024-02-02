input_string = "geekcoders geekcoders hello nikhil swati swati"

def unique_words(input_string):
    dict = {}
    output_list = []
    for word in input_string.split():
        if word in dict:
            dict[word] = dict[word]+1
        else:
            dict[word] = 1

    for k,v in dict.items():
        if v==1:
            output_list.append(k)
    return output_list

print(unique_words(input_string))