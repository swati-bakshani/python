data = "geekcoders geekcoders hello"

def unique_words(data):
    dict = {}
    for word in data.split():
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] = dict[word]+1

    return dict

if __name__ == '__main__':

    user_input = input("Enter your statement: ")
    result = unique_words(user_input)
    print(f"your result is {result}")
    for key, value in result.items():
        print(f"Count for {key} word is {value} ")
        # print(int(key), value)
    # print(f"your result is {result}")




