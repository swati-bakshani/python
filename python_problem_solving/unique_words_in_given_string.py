# Find the Unique words from the given input string

str1 = "swati is a a a data data engineer"
# output = ['swati', 'is', 'a', 'data', 'engineer'] - here everything is coming once
#             (when if condition is if(v>=1):
#                   output_list.append(k) )
# output = ['swati', 'is', 'engineer'] - - here only that are coming which are unique
#                 (when if condition is if(v==1): and one more way if v<2
#                   output_list.append(k) )
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

