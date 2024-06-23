input = "swati is a a a data data engineer"
def remove_duplicate_words(input):
    dict = {}
    output_list =[]
    for word in input.split():
        if word in dict:
            dict[word]=dict[word]+1
        elif word not in dict:
            dict[word] = 1
    for k,v in dict.items():
        if v>=1:
            output_list.append(k)
    return output_list

print(remove_duplicate_words(input))
