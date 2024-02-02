input_str= "swati is is good"
def unique_words(input_str):
    dict = {}
    output_list = []
    for i in input_str:
        if (i not in dict):
            dict[i] = 1

        else:
            dict[i] = dict[i] + 1

    for k,v in dict.items():
        if v==1:
            output_list.append(k)
    return output_list

print(unique_words(input_str))

