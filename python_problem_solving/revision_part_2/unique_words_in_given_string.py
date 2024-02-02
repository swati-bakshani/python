data = "geekcoders geekcoders hello"

def unique_words(data):
    dict = {}
    output_list = []
    for word in data.split():
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] = dict[word] + 1

    for k,v in dict.items():
        if v==1:
            output_list.append(k)

    return output_list

if __name__ == '__main__':

    user_input = input("Enter your statement: ")
    result = unique_words(user_input)
    print(f"your result is {result}")
    for item in result:
        print(f"Unieuq words from given string is: {item}")
    # for key, value in result.items():
    #     print(f"Count for {key} word is {value} ")
    #     print(int(key), value)
    # print(f"your result is {result}")




