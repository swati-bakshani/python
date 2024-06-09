input = "nikhil meghnani"
def print_consonants(list):
    output_list = []
    vowel = ["a","e","i","o","u"]
    for letter in list:
        if letter not in vowel:
            output_list.append(letter)
    return output_list

print(print_consonants(input))