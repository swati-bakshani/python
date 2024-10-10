data = "geekcoders geekcoders hello"

def count_words(data):
    dict = {}
    for word in data.split():
        if word in dict:
            dict[word] = dict[word]+1
        elif word not in dict:
            dict[word] = 1
    return dict

print(count_words(data))

user_input = input("enter your statement: ")
result = count_words(user_input)

print(result)