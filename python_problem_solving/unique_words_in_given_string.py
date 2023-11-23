# Find the Unique words from the given input string

str1 = "geekcoders geekcoders hello"

def f_unique(input_string):
    dict={}
    output_list = []
    for i in input_string.split():
        if(i not in dict):
            dict[i]=1
            # print(dict)

        else:
            dict[i]=dict[i]+1

            # print(dict)
    for k,v in dict.items():
        if(v==1):
            output_list.append(k)
    return output_list
print(f_unique(str1))